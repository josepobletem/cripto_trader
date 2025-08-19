from unittest.mock import patch  # Asegúrate de importar patch

import requests

# Reemplaza esto por tu IP pública de EC2 o Fargate si usas despliegue real
AWS_URL = "http://localhost:8000"


@patch("requests.get")
def test_aws_home_endpoint(mock_get):
    # Simula la respuesta del endpoint "/"
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = "Welcome to Crypto Trader"

    response = requests.get(f"{AWS_URL}/")
    assert response.status_code == 200
    assert "Crypto Trader" in response.text


@patch("requests.get")
def test_aws_metrics_endpoint(mock_get):
    # Simula la respuesta del endpoint "/metrics"
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = "trade_decisions_total 42"

    response = requests.get(f"{AWS_URL}/metrics")
    assert response.status_code == 200
    assert "trade_decisions_total" in response.text
