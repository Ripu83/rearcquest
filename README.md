# AWS CDK Infrastructure for ECS EC2 Cluster with ALB and Custom HTTPS Certificates

This repository contains an AWS CDK app to deploy an infrastructure for running an ECS EC2 Cluster with the following components and Quest application.
- ECS EC2 Cluster with `t2.micro` instances
- Application Load Balancer (ALB)
- Custom HTTPS certificates uploaded to AWS ACM
- Docker image from a public Docker registry


## Prerequisites

Before deploying the application, ensure that you have the following tools installed on your local machine:

1. **AWS CLI**
   - Install the AWS CLI: [Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
   - Configure AWS CLI with your credentials: 
     ```bash
     aws configure
     ```

2. **AWS CDK**
   - Install AWS CDK globally using npm:
     ```bash
     npm install -g aws-cdk
     ```

3. **Node.js & npm**
   - Install Node.js (which includes npm) from [Node.js website](https://nodejs.org/)
   - Verify the installation:
     ```bash
     node -v
     npm -v
     ```

4. **Python**
   - Ensure Python is installed: [Download Python](https://www.python.org/downloads/)

## Repository Structure

The repository consists of the following folders:
- **`quest`**: Contains the application code and `Dockerfile` for building the Docker image.
- **`CDK`**: Contains the CDK application to deploy the ECS EC2 Cluster, ALB, ACM certificates, etc.

## Deploying the CDK Application

Follow these steps to deploy the infrastructure:

1. **Install the necessary dependencies**:
   In the root folder, run the following commands to install the required Node.js dependencies:
   ```bash
   npm install
