import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")
        self.symbol = os.getenv("TRADE_SYMBOL")
        self.quantity = float(os.getenv("TRADE_QUANTITY"))
        self.client = Client(self.api_key, self.api_secret)

    def get_price(self) -> float:
        ticker = self.client.get_symbol_ticker(symbol=self.symbol)
        return float(ticker['price'])

    def place_order(self, side: str):
        if side.upper() not in ["BUY", "SELL"]:
            raise ValueError("Invalid order side")
        return self.client.create_order(
            symbol=self.symbol,
            side=side.upper(),
            type="MARKET",
            quantity=self.quantity
        )
