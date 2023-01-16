---
title: How to experiment with MLFlow locally on laptop or PC? Instructions for the local setup.
slug: how-to-experiment-with-mlflow-locally-on-laptop-or-pc
date: 2023-01-14
modified: 2023-01-14
status: published
tags: mlops, mlflow, machine-learning 
summary: summary
category: note
citation_needed: false
---
To set up MLFlow locally on your laptop or PC, you will need to have Python and pip (the package installer for Python) installed.

1.  First, install MLFlow using pip by running the command `pip install mlflow` in your terminal or command prompt.
    
2.  Next, create a new Python script or open an existing one that you want to use to experiment with MLFlow.
    
3.  Import the mlflow library in your script by adding the following line at the top of your script: `import mlflow`.
    
4.  Start an MLFlow run by adding the following line at the beginning of your script: `mlflow.start_run()`.
    
5.  Throughout your script, use the mlflow library to log parameters, metrics, and artifacts (such as model files) as your script runs. For example, you can log a parameter by adding the following line: `mlflow.log_param("parameter_name", parameter_value)`
    
6.  End the run by adding `mlflow.end_run()` at the end of your script
    
7.  To view the run, you can run `mlflow ui` to open the web UI locally on your browser.
    
8.  To run your script with the mlflow command line tool, you can use `mlflow run [path to your script]`

Note: To use other features like tracking and model registry, you need to set up a MLFlow server.

## Using an MLFlow server from your local machine
There are several alternatives for using an MLFlow server on your local machine, including:

### 1.  Using a cloud-based MLFlow service
Some cloud providers, such as AWS and GCP, offer managed MLFlow services that can be used to track and manage your machine learning experiments. These services typically include features such as automatic scaling, data storage and backup, and integration with other cloud-based services.
    
### 2.  Deploying MLFlow on a virtual machine
You can set up a virtual machine (VM) on a cloud provider or on-premises and install MLFlow on it. This allows you to have more control over the server's resources and configuration, and also allows you to run MLFlow on your own infrastructure.
    
### 3.  Using a containerization technology like Docker
You can containerize your MLFlow server using Docker and run it on any machine. This allows you to easily move your server to different environments and ensures that the server's dependencies are isolated.
    
### 4. Using a Kubernetes-based deployment
You can use Kubernetes, an open-source container orchestration system, to deploy MLFlow on a cluster of machines. This allows you to scale your server horizontally and ensures high availability.
    
Ultimately, the best option for you will depend on your specific use case, budget, and technical requirements.

Docker container + mounted volumes for persistence of data served best for my case.