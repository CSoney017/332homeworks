# HOMEWORK 07: In The Kubernetes

## Overview: 

Homework 07 is based loosely off of homework 06, identifying genes based off of the 
Human Genome Organization (HUGO) Genome Nomenclature Committee Dataset found 
[here](https://www.genenames.org/download/archive/). In addition to the Flask application
in homeowrk 06, it can also be deployed with Redis using a Kubernetes Cluster. 

This project contains this README, the Dockerfile, and docker-compose.yml file,
and the redis deployment/pvc/service files, flask deployment/service file, and a debug python deployment file. 

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
provided in this repository. Use the command 
`$ docker build -t <username>/hgnc_id .`. 
Replace <username> with your Docker Hub username both in the command listed above
and also in the docker-compose.yml file in the line `image: <username>/gene_api:1.0`. .
Run the image with 
`$ docker run -it --rm -p 5000:5000 <username>/hgnc_api:k8s .`. 

### docker-compose 
To launch the app using Redis, use the command
`$ docker-compose up -d`.

To terminate the app, use 
`$ docker-composes down`. 

### Kubernetes 
To run the app on Kubernetes (K8S), please use the following command: 
`$ kubectl apply -f <file_name>`. 

Replace file name with the Redis deployment/pvc/service file. Please do this with the Flask and python debug deployment files as well. 
Each `.yml` should have been applied. 

To confirm that the pods are running, use the command
`$ kubectl get pods`. 

The result should be similar to the one shown below: 

```
{
$ kubectl get pods
NAME                                            READY   STATUS    RESTARTS   AGE
csy017-test-redis-deployment-8bfd9bf7b-d6hv8    1/1     Running   0          6h4m
py-debug-deployment-f484b4b99-qf9kz             1/1     Running   0          6h6m
test-csy017-flask-deployment-5589676dcf-7t2h2   1/1     Running   0          5h45m
test-csy017-flask-deployment-5589676dcf-8g8pm   1/1     Running   0          5h45m
}
```

In addition to the status of the pods, it will also return the identification series of each pod. 

Access the python debug deployment file to use the K8S cluster: 
`$ kubectl exec -it <python_deployment_file> -- /bin/bash` 

This will redirect you into a terminal where you may now curl each of the 
routes, such as this one: 

```
{
$ kubectl exec -it py-debug-deployment-f484b4b99-qf9kz -- /bin/bash
root@py-debug-deployment-f484b4b99-qf9kz:/#
}
```
This is where you may `curl` any of the routes. However, please note that instead 
of using the usual `localhost`, you must replace it with `csy017-test-flask-service`. 
