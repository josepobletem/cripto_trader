terraform {
  required_providers {
    null = {
      source = "hashicorp/null"
      version = "3.2.1"
    }
  }
}

provider "null" {}

resource "null_resource" "simulate_aws_ec2" {
  provisioner "local-exec" {
    command = "echo 'Simulando despliegue en AWS EC2 en región ${var.region}'"
  }
}
