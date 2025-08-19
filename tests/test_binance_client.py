from unittest.mock import patch

from trading.binance_client import BinanceClient


@patch("trading.binance_client.Client")
def test_get_price(mock_client_class):
    mock_client = mock_client_class.return_value
    mock_client.get_symbol_ticker.return_value = {"price": "31000.0"}
    binance = BinanceClient()
    price = binance.get_price()
    assert price == 31000.0
