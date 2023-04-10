import requests
import redis
import json
from flask import Flask, request

app = Flask(__name__)

def get_redis_client():
 '''
 required function to use redis
 '''
 return redis.Redis(host='127.0.0.1', port = 6379, db = 0, decode_responses = True)

rd = get_redis_client()

@app.route('/plot', methods = ['GET'])
def plot_redis():

 import matplotlib.pyplot as plt
 import numpy as np

 x = np.linspace(0, 2*np.pi, 50)
 plt.plot(x, np.sin(x))
 plt.savefig('my_sinwave.png')

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

   # global data
   reponse = requests.get(url = 'https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
   rd = get_redis_client()

   for item in response.json()['response']['docs']:
     key = f'{item["hgnc_id"]}'
     rd.set(item.get('hgnc_id'), json.dumps(item))

   return 'data has been loaded'

 elif request.method == 'GET':

   rd = get_redis_client()
   output_list = []

   for item in rd.keys():
     output_list.append(json.loads(rd.get(item)))
   return output_list

 elif request.method == 'DELETE':
   rd.flushdb()
   return 'data has been cleared'

 else:
  return "the method entered is unrecognized"

@app.route('/genes', methods = ['GET'])
def all_hgnc() -> list:

 '''
 returns a list of all hgnc_id fields

 Args:
   none

 Returns:
   gene_id(list): contains all the hgnc_id fields
 '''
 # data = get_data()  # how can I ensure the data has been loaded?
 gene_id = []
 for x in rd.keys():
   gene_id.append(x)
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

 # gene_id = all_hgnc()
 retrieve_gene = {} # will the retrieved information be in list format?

 # do i need to have this try-except block? wouldn't the id be processed as a string anyway?
 try:
  hgnc_id = str(hgnc_id)
 except typeError:
  return 'Error: please enter a string for the desired hgnc_id'

 # try:
 #  for ii in gene_id:
 #    if ii['hgnc_id'] == hgnc_id:
 #       should it be an if statement?

 # except unknownID:
 #  return 'Error: hgnc_id could not be found'

 for ii in gene_id:
   if ii['hgnc_id'] == hgnc_id:
     retrieve_gene.append(ii)

 return retrieve_gene

@app.route('/genes/<int:hgnc_id>', methods = ['GET'])
def get_gene_info(gene_id):
 '''
 returns data associated with a specified gene

 Arg:
   gene_id(int): user-entered gene id

 Returns:
   gene_info(dict): all data associated with a specific gene
 '''

 id_str = "HGNC:" + id_num
 gene_data = []
 hgnc_data = []

 for item in rd.keys():
   hgnc_data.append(json.loads(rd.get(item)))
 for ii in hgnc_data:
   if point == id_str:
     gene_info = json.dumps(point)
 return gene_info

if __name__ == '__main__':
   app.run(debug=True, host = '0.0.0.0')
