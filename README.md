# FastAPI App Deployment to AWS Fargate using GitHub Actions

This repository contains the code and CI/CD pipeline configuration for deploying a FastAPI application to AWS Fargate using GitHub Actions. The deployment process involves building a Docker image of the FastAPI app, pushing the image to Amazon ECR (Elastic Container Registry), and updating the Fargate service to use the new image.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Deployment Workflow](#deployment-workflow)

## Prerequisites

Before you start, ensure you have the following:

1. **AWS Account**: An active AWS account with necessary permissions to create and manage ECS services and ECR repositories.
2. **AWS CLI**: Installed and configured on your local machine with access to your AWS account.
3. **Docker**: Installed on your local machine for building and testing Docker images locally.
4. **GitHub Repository Secrets**: Set up the following secrets in your GitHub repository:
   - `AWS_ACCESS_KEY_ID`: Your AWS access key.
   - `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key.
   - `AWS_REGION`: The AWS region where your ECR and Fargate services are located.
   - `ECR_REPOSITORY`: The name of your ECR repository.
   - `ECS_CLUSTER`: The name of your ECS cluster.
   - `ECS_SERVICE`: The name of your ECS service.

## Deployment Workflow

The CI/CD pipeline involves the following steps:

1. **Build Docker Image**: The FastAPI application is containerized using Docker.
2. **Push Docker Image to ECR**: The built Docker image is pushed to Amazon ECR.
3. **Update Fargate Service**: The ECS Fargate service is updated to use the latest Docker image.
