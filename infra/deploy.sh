#!/bin/bash

echo "Deploying Multi-Cloud FinOps Infrastructure..."

# Initialize Terraform
terraform init

# Apply Terraform configuration
terraform apply -auto-approve

echo "Deployment complete!"
