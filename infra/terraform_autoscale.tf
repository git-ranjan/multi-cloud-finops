# Auto-scaling & cost reduction Terraform configuration

resource "aws_autoscaling_group" "finops_asg" {
  name                 = "finops-autoscale-group"
  max_size             = 5
  min_size             = 1
  desired_capacity     = 2
}

resource "google_compute_instance_group_manager" "finops_gcp_asg" {
  name       = "finops-gcp-asg"
  base_instance_name = "finops-instance"
  target_size = 2
}

resource "azurerm_virtual_machine_scale_set" "finops_azure_asg" {
  name                = "finops-azure-asg"
  location            = "East US"
  resource_group_name = "your-resource-group"
  sku {
    name     = "Standard_B2s"
    capacity = 2
  }
}
