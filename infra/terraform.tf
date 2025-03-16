# Terraform configuration file for Multi-Cloud FinOps

provider "aws" {
  region = "us-east-1"
}

provider "google" {
  project = "your-gcp-project"
  region  = "us-central1"
}

provider "azurerm" {
  features {}
}

resource "aws_s3_bucket" "finops_logs" {
  bucket = "multi-cloud-finops-logs"
  acl    = "private"
}

resource "google_storage_bucket" "finops_logs" {
  name          = "multi-cloud-finops-logs"
  location      = "US"
  storage_class = "STANDARD"
}

resource "azurerm_storage_account" "finops_logs" {
  name                     = "multicloudfinops"
  resource_group_name      = "your-azure-resource-group"
  location                 = "East US"
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

output "aws_s3_bucket" {
  value = aws_s3_bucket.finops_logs.id
}

output "gcp_storage_bucket" {
  value = google_storage_bucket.finops_logs.id
}

output "azure_storage_account" {
  value = azurerm_storage_account.finops_logs.id
}
