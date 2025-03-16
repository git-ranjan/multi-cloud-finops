#!/bin/bash

echo "Destroying Multi-Cloud FinOps Infrastructure..."

# Destroy Terraform-managed resources
terraform destroy -auto-approve

echo "Infrastructure destroyed!"
