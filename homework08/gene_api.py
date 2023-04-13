from flask import Flask, request
import redis
import requests
import json
import os
from matplotlib import pyplot as plt
import numpy as np

app = Flask(__name__)

def get_redis_client():
 redis_ip = os.environ.get('REDIS_IP')
 if not redis_ip:
    raise Exception()
 return  redis.Redis(host=redis_ip, port=6379, db=0)

 #return redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)
rd = get_redis_client()
rd_img = get_redis_client(1, False)

@app.route('/data', methods=['GET', 'POST', 'DELETE'])
def get_route():
    """
    posts, outputs, or deletes all data in Redis depending on method used

    Args:
      None

    Returns:

       Method:

           POST:
             (string): 'data has been loaded'

           GET:
              data(list): list containing all hgnc_ids

           DELETE:
              (string): 'data has been deleted'
    """

    if request.method == 'GET':
        data = []

        for item in rd.keys():
            data.append(json.loads(rd.get(item)))

        return data

    elif request.method == 'POST':
        response = requests.get('https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')

        for item in response.json()['response']['docs']:
            key = f'{item["hgnc_id"]}'
            item = json.dumps(item)
            rd.set(key, item)

        return f'Data has been loaded'

    elif request.method == 'DELETE':
        rd.flushdb()

        return f'Data has been deleted'

    else:
        return 'invalid method'

@app.route('/genes', methods=['GET'])
def get_genes() -> list:
    """
    returns json-formatted list of all hgnc_ids

    Args:
      None

    Returns
        gene_id(list): contains all hgnc_id fields
    """

    return rd.keys()

@app.route('/genes/<string:hgnc_id>', methods=['GET'])
def get_hgnc_id(hgnc_id:str) -> dict:
    """
    returns a specified gene

    Args:
      hgnc_id (str):  hgnc id of a gene

    Returns:
        gene_info (dict): information on the specified gene
    """
    if rd.get(hgnc_id) == None:
        return 'ERROR: specified id is not a gene in the dataset'

    output = json.loads(rd.get(hgnc_id))
    return output

@app.route('/image', methods=['GET', 'POST', 'DELETE'])
def get_image():
    """
    depending on specified method, creates and deletes images on Redis database

    Args:
      None
    Returns:
        image(png): pie chart of gene location.
    """
    # GET METHOD
    if request.method == 'GET':

        if rd_img.exists('image'):

            path = './image.png'

            with open(path, 'wb') as f:
                f.write(rd_img.get('image'))
            return send_file(path, mimetype='image/png', as_attachment=True)

        else:
            return 'no images found.\n', 400

    # POST METHOD
    elif request.method == 'POST':

        if len(rd.keys())==0:
            return 'data is nonexistant. plot cannot be created\n', 400

        location = {}

        for item in rd.keys():
            item = json.loads(rd.get(item))

            if item['locus_group'] not in location:
                location[item['locus_group']]=1

            else:
                location[item['locus_group']]+=1

        genes = []
        data = []

        for key in location.keys():
            genes.append(key)
            data.append(location[key])

        plt.figure()
        plt.pie(data, labels=genes)
        plt.title('HGNC Genes Dataset')
        plt.savefig('./image.png')
        filebytes = open('./image.png', 'rb').read()
        rd_img.set('image', filebytes)
        return 'plot has been created.\n'

    # DELETE METHOD
    elif request.method == 'DELETE':
        rd_img.flushdb()
        return 'plot has been deleted.\n'
    else:
        return 'Specified method is invalid.', 400

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
