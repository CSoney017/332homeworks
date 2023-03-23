# Homework 06: Say It Ain't Genes

## Overview

Homework 06 is based off the dataset found [here](https://www.genenames.org/download/archive/)
and inputting the data into a Redis application. This project contains the python script
`genes_redis.py`, a Dockerfile, docker-compose file labeled `docker-compose.yml`, and this README. 

## Routes

The python script in this repository contains 3 routes: `/data`, `/genes`, and `/genes/<hgnc_id>`.

- The `/data` route uses three different methods to return three different results. 

** Different Methods:**

 1. POST
   Using the 'POST' method initializes the data into Redis

 2. GET
   This method will return the previously initialized data from Redis

 3. DELETE
   'DELETE' will delete the intialized data from Redis

- `/genes` will return a json-formatted list of all hgnc_ids

- `/genes/<hgnc_id>` will return all data associated with a specified <hgnc_id>


## Docker Hub

To run this app on Docker Hub, please pull the image using the command 
`docker pull <username>/hgnc_id`. Next, build the image using
`docker build -t csoney017/hgnc_id`. 

## Dockerfile

Another way to run this project is to build your own image using the Dockerfile 
provided in this repository. Us ethe command `docker build -t <username>/hgnc_id .`. Replace <username> with your Docker Hub username.
Run the image with `docker run -it --rm -p 5000:5000 <username>/hgnc_id .`. 


