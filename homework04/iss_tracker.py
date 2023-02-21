from flask import Flask

import requests
import xmltodict
import math

app = Flask(__name__)

def get_data() -> dict:
  """
  Enters data from XML file into dictionary

  Args:
     none

  Returns:
     iss_data(dict): data in XML file converted into a python dictionary
  """

  response = requests.get(url = 'https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml')
  data = xmltodict.parse(response.text)
  return data

@app.route('/', methods = ['GET'])
def total_data() -> dict:
   """
   Returns data in XML file as a python dictionary

   Args:
     none

   Returns:
      iss_data(dict): data in XML file converted into a python dictionary
   """

   iss_data = get_data()
   return iss_data

@app.route('/epochs', methods = ['GET'])
def epochs_only() -> list:
 """
 Returns a list of all the epoch values in

 Args:
  none

 Return:
  epochs(list): a list of all defined epoch values
 """

 iss_data = get_data()
 epochs = [] # initializing list to store epochs
 data = []
 #accessing only the stateVector data

 data = iss_data['ndm']['oem']['body']['segment']['data']['stateVector']

 for ii in data:
  epochs.append(ii['EPOCH'])
 return epochs

@app.route('/epochs/<epoch>', methods = ['GET'])
# the less than/greater than sign means that it's a specific value we're hunting for
def stateVectors(epoch: str) -> dict:
   """
   prints out block of data detailing position and velocity for a specific epoch

   args:
     epoch(str): a specific time within the data

   returns:
    a dictionary with data containting position (x,y,z) and velocity (x_dot, y_dot, and z_dot) at a specific time (epoc)
   """

   iss_data = get_data()
   iss_data = iss_data['ndm']['oem']['body']['segment']['data']['stateVector']
   output = {} # curly brackets = intializing dictionary

   for ii in iss_data:
     if ii['EPOCH'] == epoch: # searching for specific EPOCH
       output = ii # entering epoch into dict

       for jj in output:

         if jj != 'EPOCH': #inserting value into dict
           output[jj] = float(output[jj]['#text'])

   return output

@app.route('/epochs/<epoch>/speed', methods = ['GET'])
def calc_speed(epoch) -> str:
   """
   Returns the speed at a specific time

   Args:
    epoch(str): a specific time

   Returns:
    speed(str): an int typecasted to a string that calculates the speed at a specific point in time (epoch)
   """
   data = {}
   data = stateVectors(epoch) # calling function stateVectors

   if len(data) > 0:
     speed = math.sqrt(data['X_DOT']**2 + data['Y_DOT']**2 + data['Z_DOT']**2)
     return str(speed)

   else:
     return "Error"

if __name__ == '__main__':
   app.run(debug = True, host = '0.0.0.0')
