# SimpleTimeService - Dockerized AWS ECS Deployment with Terraform
This repository contains a simple microservice, SimpleTimeService, which provides the current UTC timestamp and the requester's IP address. It is Dockerized for easy deployment, and infrastructure is managed via Terraform to deploy it on AWS ECS (Fargate).

#Overview
SimpleTimeService: A Flask app that responds with a JSON object containing the current timestamp and the client's IP address.

Dockerized: The application is packaged in a Docker container for seamless deployment.

Terraform Infrastructure: Terraform is used to provision the AWS resources required for hosting the service, including:

VPC with public and private subnets.

ECS Fargate Cluster running the service in private subnets.

Application Load Balancer (ALB) to route traffic to ECS tasks.

#Setup and Deployment
1. Dockerize the Application
The application is packaged in a Docker container for easy deployment. The Dockerfile ensures that the application runs as a non-root user inside the container.

2. Terraform Infrastructure Setup
The Terraform configuration will provision the necessary infrastructure in AWS. This includes:

VPC with public and private subnets.

ECS Fargate Cluster to run the Docker container.

Application Load Balancer to route HTTP requests to the ECS tasks.

Steps for Deployment:
Clone the repository.

Configure the AWS region and Docker image name in the terraform.tfvars file.

Initialize the Terraform environment by running terraform init.

Apply the configuration with terraform apply to deploy the infrastructure.

After deployment, the Load Balancer URL will be provided, which you can use to access the service.

3. Access the Service
Once the deployment is successful, access the service via the provided Load Balancer URL in your browser. The service will return a JSON response like:

json
Copy
Edit
{
  "timestamp": "current-utc-time",
  "ip": "client-ip-address"
}
File Structure
The repository is structured as follows:

main.tf: Core infrastructure resources.

variables.tf: Terraform variables for configuration.

terraform.tfvars: Variable values (AWS region, Docker image).

outputs.tf: Output values, including the Load Balancer URL.

Dockerfile: The Dockerfile for packaging the Flask app.

app.py: The Python code for the Flask app.

requirements.txt: Python dependencies.

License
MIT License.

Author
Your Name

