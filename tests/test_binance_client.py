from unittest.mock import patch

from trading.binance_client import BinanceClient


@patch("trading.binance_client.Client")
@patch("os.getenv")
def test_get_price(mock_getenv, mock_client_class):
    # Simula las variables de entorno
    mock_getenv.side_effect = lambda key: {
        "BINANCE_API_KEY": "test_api_key",
        "BINANCE_API_SECRET": "test_api_secret",
        "TRADE_SYMBOL": "BTCUSDT",
        "TRADE_QUANTITY": "0.01",
    }.get(key)

    # Simula el cliente de Binance
    mock_client = mock_client_class.return_value
    mock_client.get_symbol_ticker.return_value = {"price": "31000.0"}

    # Instancia BinanceClient
    binance = BinanceClient()

    # Llama al método get_price
    price = binance.get_price()

    # Verifica que el precio sea el esperado
    assert price == 31000.0
