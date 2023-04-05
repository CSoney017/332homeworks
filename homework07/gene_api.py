from flask import Flask, request
import redis
mport requests
import json

app = Flask(__name__)

def get_redis_client():
    """
    This function creates a connection to a Redis database
    
    Arguments
        None
    Returns
        redis_database (redis.client.Redis): Redis client
    """
    return redis.Redis(host='klajoie-test-redis-service', port=6379, db=0, decode_responses=True)

rd = get_redis_client()

@app.route('/data', methods=['GET', 'POST', 'DELETE'])
def get_route():
    """
    This function either posts, outputs, or deletes all data in the Redis database.

    Arguments
        None
    Returns
        None
    """
    if request.method == 'GET':
        output_list = []
        for item in rd.keys():
            output_list.append(json.loads(rd.get(item)))
        return output_list
    elif request.method == 'POST':
        response = requests.get('https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
        for item in response.json()['response']['docs']:
            key = f'{item["hgnc_id"]}'
            item = json.dumps(item)            
            rd.set(key, item)
        return f'Data loaded, there are {len(rd.keys())} keys in the db.\n'
    elif request.method == 'DELETE':
        rd.flushdb()
        return f'Data deleted, there are {len(rd.keys())} keys in the db.\n'
    else:
        return 'The method you requested does not apply.\n', 400

@app.route('/genes', methods=['GET'])
def get_genes() -> list:
    """
    This function returns all of the keys in the Redis database.

    Arguments
        None
    Returns
        keys (list): unordered list of all keys in the database
    """

    return rd.keys()

@app.route('/genes/<string:hgnc_id>', methods=['GET'])
def get_hgnc_id(hgnc_id:str) -> dict:
    """
    This function retrieves a specific gene from the database.

    Arguments
        hgnc_id (str):  HGNC ID of the gene, EX. HGNC:35458
    Returns
        gene_info (dict): all HGNC approved information on the requested gene
    """
    if rd.get(hgnc_id) == None:
        return f'{hgnc_id} is not a gene in the dataset. Please try another.\n', 400

    ret = json.loads(rd.get(hgnc_id))
    return ret

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
