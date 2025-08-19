import requests

# Reemplaza esto por tu IP pública de EC2 o Fargate si usas despliegue real
AWS_URL = "http://localhost:8000"


def test_aws_home_endpoint():
    response = requests.get(f"{AWS_URL}/")
    assert response.status_code == 200
    assert "Crypto Trader" in response.text


def test_aws_metrics_endpoint():
    response = requests.get(f"{AWS_URL}/metrics")
    assert response.status_code == 200
    assert "trade_decisions_total" in response.text
