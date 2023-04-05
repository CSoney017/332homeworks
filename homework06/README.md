# Homework 06: Say It Ain't Genes

## Overview

Homework 06 is based off the dataset found [here](https://www.genenames.org/download/archive/)
and inputting the data into a Redis application. 
The data chosen for this project was created by the HUGO Gene Nomenclature Committee with the intention of creating
a uniqure and meaningful name for every gene.
This project contains the python script
`genes_redis.py`, a Dockerfile, docker-compose file labeled `docker-compose.yml`, and this README. 

## Routes

The python script in this repository contains 3 routes: `/data`, `/genes`, and `/genes/<hgnc_id>`.

- The `/data` route uses three different methods to return three different results. 

  **Different Methods:**

  1. POST
     Using the 'POST' method initializes the data into Redis

  2. GET
     This method will return the previously initialized data from Redis

  3. DELETE
     'DELETE' will delete the intialized data from Redis

- `/genes` will return a json-formatted list of all hgnc_ids

- `/genes/<hgnc_id>` will return all data associated with a specified <hgnc_id>


## Running the Project
** note: ** before attempting to run this project, please ensure the GitHub repository has been cloned using the command:
`git clone git@github.com:CSoney017/332homeworks.git`. 

### Docker Hub

To run this app on Docker Hub, please pull the image using the command 
`docker pull csoney017/gene_api`. Run the image with `docker run -it --rm csoney017/gene_api:1.0`. 

### Dockerfile

Another way to run this project is to build your own image using the Dockerfile 
provided in this repository. Use the command `docker build -t <username>/hgnc_id .`. 
Replace <username> with your Docker Hub username both in the command listed above
and also in the docker-compose.yml file in the line `image: <username>/gene_api:1.0`. .
Run the image with `docker run -it --rm -p 5000:5000 <username>/gene_api:1.0 .`. 


