
# Homework 04: Buddy Flask

## objective:
The purpose of this homework assignment is to build a Flask application 
for querying and returning interesting information from the ISS data set. This project
contains this README file and the python script 'iss_tracker.py'. 

## Flask:
Flask in an application that receives a request from a client which the 
framework recognizes and runs calculations which will return a result. 

## Accessing Data:
The data used for this project was taken from the [ISS Trajectory Data] (https://spotthestation.nasa.gov/trajectory_data.cfm) website.\
It is accessed in the XML format. The data is categorized into the position and velocity depending on the epochs. 

## Running the App:
To run this app, please ensure that you have the requests, flask, and xmltodict libraries installed. 
This can be done using
`pip3 install --user <library_name>` 

Once that is completed, run the following command in the same directory as the `iss_tracker.py` file: 

`flask --app iss_tracker --debug run` 

In another terminal, different functions can be called using the following commands: 

```
curl localhost:5000/
curl localhost:5000/epochs
curl localhost:5000/epochs/<epoch>
curl localhost:5000/epochs/<epoch>/speed
```

## Results:

The first route `curl localhost:5000/` will return all the data in the XML file as a dictionary. 

The second route `curl localhost:5000/epochs` will only display an output of all the epochs with 
their positions (ex: x and x_dot). 

The third route `curl localhost:5000/epochs/<epoch>` will return the data for one specific epoch data block. 

The last route will return the velocity calculated at the specific epoch. 
