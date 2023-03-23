import requests
import redis

from flask import Flask, request

app = Flask(__name__)

def get_redit_client():
 '''
 required function to use redis
 '''

  return redis.Redis(host='127.0.0.1', port = 6379, db = 0, decode_responses = True)
rd = get_redis_client()

@app.route('/data', methods = ['POST', 'GET', 'DELETE'])
def get_data():
 '''
 initializes, retrieves, or deletes data depending on method used

 Args: none

 Returns:

   Method:

     POST:
      (string)"data has been loaded"

     GET:
       data (list of dictionaries)

     DELETE:
       (string) "data has been deleted"
 '''

 if request.method == 'POST':

   global data
   reponse = requests.get(url = 'https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
   data = json.loads(response.text)

   for item in response.json():
     rd.set(d['id'], json.dumps(d))

 return 'data has been loaded'

 if request.method == 'GET':

   output_list = []

   for x in data['archive']
     output_list.append(json.loads(rd.get(x['id'])))

 return (json.dumps(output_list, indent = 1) ) # can't i also just do return output_list?

 if request.method == 'DELETE':
   data.clear()
 return 'data has been cleared'

@app.route('/genes', methods = ['GET'])
def all_hgnc() -> list:

 '''
 returns a list of all hgnc_id fields

 Args:
   none

 Returns:
   gene_id(list): contains all the hgnc_id fields
 '''

data = get_data() # how do I call the function intending to use the POST method?

 gene_id = []
 for x in data['hgnc_id']
   gene_id.append(json.loads(rd.get(x['id'])))

 return gene_id

@app.route('/genes/<hgnc_id>', methods = ['GET'])
def hgnc_id(hgnc_id) -> dict:
 '''
 returns data associated with a given <hgnc_id>

 Args:
   hgnc_id(string): a specific gene id

 Returns:
   retrieve_gene(dict): a dictionary containing all the information for the <hgnc_id>
 '''

 gene_id = all_hgnc()
 retrieve_gene = {} # will the retrieved information be in list format?

 # do i need to have this try-except block? wouldn't the id be processed as a string anyway?
 try:
  hgnc_id = str(hgnc_id)
 except typeError:
  return 'Error: please enter a string for the desired hgnc_id'

 try:
   for ii in gene_id:
     if ii['hgnc_id'] == hgnc_id
       # should it be an if statement?

 except unknownID:
   return 'Error: hgnc_id could not be found'

 for ii in gene_id:
   if ii['hgnc_id'] == hgnc_id:
     retrieve_gene = ii

     for jj in gene_id:

       if jj != 'hgnc_id':
         output[jj] = float(output[jj]['#text'])

if __name == '__main__':
   app.run(debug=True, host = '0.0.0.0')
