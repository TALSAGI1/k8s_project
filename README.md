This project demonstrates the implementation of fundamental Kubernetes concepts using a simple Python web application. The goal is to provide a complete and practical example of the application lifecycle, from building a Docker image to deploying and managing resources within a Kubernetes cluster.

Core Project Components 🧩
The project is built upon several key Kubernetes objects, each serving a critical role in the application's deployment:

Dockerfile: This file contains all the necessary instructions to build the Docker image for the Python application. It defines the runtime environment, dependencies, and the main command to run the application.

Python Application (Flask): A lightweight web application configured to consume data from a ConfigMap and a Secret via environment variables. The app also includes essential liveness (/healthz) and readiness (/ready) probes for Kubernetes to monitor its health.

Kubernetes YAML: A single YAML file that defines the entire deployment configuration:

Namespace: A dedicated namespace called dev-project to isolate all project resources from the rest of the cluster.

ConfigMap & Secret: Objects used to decouple configuration data and sensitive information from the application's code, ensuring flexibility and security.

Deployment: Manages the application's deployment by creating and maintaining a desired number of Pod replicas.

Service: Exposes the application using a stable internal IP address and a NodePort, allowing for external access to the application.

Getting Started 🛠️
To run this project, follow these steps:

Build the Docker Image:

Bash

docker build -t my-app:latest .
Deploy to Kubernetes:

Bash

kubectl apply -f full-app.yaml
Verify the Deployment:
Check that all objects are running in the correct namespace:

Bash

kubectl get all -n dev-project
Access the Application:
Find the Minikube IP address and the assigned NodePort for your service:

Bash

minikube ip
kubectl get service my-app-service -n dev-project
Then, navigate to your browser and enter the following address: http://[minikube-ip]:[nodeport]
