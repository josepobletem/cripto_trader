terraform {
  required_providers {
    null = {
      source = "hashicorp/null"
      version = "3.2.1"
    }
  }
}

provider "null" {}

resource "null_resource" "simulate_cloud_run" {
  provisioner "local-exec" {
    command = "echo 'Simulando despliegue en Cloud Run para ${var.project}'"
  }
}