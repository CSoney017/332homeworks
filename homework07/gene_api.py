from flask import Flask, request
import redis
import requests
import json

app = Flask(__name__)

def get_redis_client():
    """
    connecting to Redis

    Args:
      None
    Return:
        redis_database (redis.client.Redis): Redis client
    """

    return redis.Redis(host='csy017-test-redis-service', port=6379, db=0, decode_responses=True)

rd = get_redis_client()

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

    ret = json.loads(rd.get(hgnc_id))
    return ret

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
