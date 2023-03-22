import requests
import redis

from flask import Flask, request

app = Flask(__name__)

def get_redit_client():
  return redis.Redis(host='127.0.0.1', port = 6379, db = 0, decode_responses = True)
rd = get_redis_client()

@app.route('/data', methods = ['POST', 'GET', 'DELETE'])
def get_data():

 if request.method == 'POST':
   reponse = requests.get(url = 'https://www.genenames.org/download/archive/')
   data = .parse(response.text)
   for item in response.json():
     key = f'{item["name"]}:{item["id"]}'
     rd.hset(k1, mapping= item)
 return 'data has been loaded'

 if request.method == 'GET':
   # output_list = []

 return data

 if request.method == 'DELETE':
   data.clear()
 return 'data has been cleared'

if __name == '__main__':
   app.run(debug=True, host = '0.0.0.0')
