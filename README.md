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

## Dockerfile in `quest` Folder

The Dockerfile for your application is located in the `quest/Dockerfile` folder


## Deploying the CDK Application

Follow these steps to deploy the infrastructure:

1. **Install the necessary dependencies**:
   In the CDK folder, run the following commands to install the required Node.js dependencies:
   ```bash
   npm install -r requirements.txt
   ```
2. **Bootstraping the AWS Account**:
   In CLI run the following commands to bootstrap account to run CDK app for first time:
   ```bash
   npm install -r requirements.txt
   ```
3. In the CDK folder, run the following commands to Deploy the CDK Stack:
   ```bash
   cdk deploy
   ```
## Deployment Instructions

1. Clone the Repository:

``` bash
Copy code
git clone https://github.com/Ripu83/rearcquest
cd rearcquest
```

2. Manual Changes Required to Deploy the Stack

  1. Update Account ID and Region in  
  to rearc_cdk/quest_ecs_ec2.py:
    Before deploying the stack, you must update the ACM ARN in the stack file.

    Open rearc_cdk/quest_ecs_ec2.py.
  Locate the placeholder for the ACM ARN:
  python
  ```acm_certificate_arn = "replace-with-your-acm-arn"```


3. Synthesize the CloudFormation Template:
Generate the CloudFormation template to ensure the stack is set up correctly:

```bash
cdk synth
```
4. Deploy the CDK Stack: 
```bash
cdk deploy
```


