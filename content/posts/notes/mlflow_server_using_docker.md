---
Category: note
Date: '2023-01-16'
Modified: '2023-07-12'
Prompt: How to deploy mlflow server on local machine using Docker. Give me text in markdown format including links, hotlinked images or other means to make article more appealing.
Slug: deploying-mlflow-on-local-machine-using-docker
Status: published
Tags: mlflow, machine-learning, mlops, docker
Title: Deploying MLFlow on Local Machine Using Docker
---

Docker is a popular tool that allows you to package, deploy, and run your applications in containers. In this tutorial, we will show you how to use Docker to deploy an MLFlow server on your local machine.

### Prerequisites

-   [Docker](https://www.docker.com/) should be installed on your local machine. If it's not installed please follow [these instructions](https://docs.docker.com/get-docker/) to install it.

### Steps

#### 1. Pull the MLFlow Docker Image

The first step is to pull the MLFlow Docker image from the official repository. You can do this by running the following command in your terminal:

```sh
docker pull atcommons/mlflow-server
```

This command downloads the latest MLFlow image from the Docker Hub.

#### 2. Run the MLFlow Image as a Container

Once you have the MLFlow image, you can run it as a container by executing the following command:

```sh
docker run --rm -p 5000:5000 atcommons/mlflow-server
```

This command starts a container from the `mlflow/mlflow` image and maps port 5000 on the host to port 5000 in the container. The `--rm` flag tells Docker to remove the container when it exits.

#### 3. Access the MLFlow Web UI

Once the container is running, you can access the MLFlow web UI by opening a web browser and navigating to `http://localhost:5000`. You should see the MLFlow web UI, as shown below:

![MLFlow Web UI](https://mlflow.org/docs/latest/images/mlflow_tracking.png)

#### 4. Run MLFlow commands

You can also use the container to run your MLFlow commands by running:

```
docker run -it --rm -p 5000:5000 mlflow/mlflow mlflow [command]
```

This command runs the specified `mlflow [command]` in the container.

#### 5. Configure the Tracking URI

To use the container as a remote server, you need to configure the tracking URI. You can set the tracking URI to the container's IP address, which you can find by running

```sh
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_name_or_id
```

#### 6. Stop the Container

To stop the container, you can find the container id by running `docker ps` then stop the container by running `docker stop container_id`

#### 7. Persist Data

To persist the data, you can use volumes. For example, you can run


```sh
docker run -p 5000:5000 -v /path/on/host:/path/on/container mlflow/mlflow` 
```

to map the host directory `/path/on/host` to the container directory `/path/on/container`.

> **NOTE**:  Running MLFlow on Docker on your local machine will not give you the ability to scale horizontally or ensure high availability. You may want to consider using cloud-based MLFlow services or deploying MLFlow on a virtual machine for more production-ready


X::[[mlFlow]]
X::[[How_to_experiment_with_MLFlow _locally_on laptop_or_PC_instructions_for_the_local_setup]]