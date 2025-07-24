import requests

# Reemplaza esto por tu URL real de Cloud Run si usas despliegue real
GCP_URL = "http://localhost:8000"

def test_gcp_home_endpoint():
    response = requests.get(f"{GCP_URL}/")
    assert response.status_code == 200
    assert "Crypto Trader" in response.text

def test_gcp_metrics_endpoint():
    response = requests.get(f"{GCP_URL}/metrics")
    assert response.status_code == 200
    assert "trade_decisions_total" in response.text
