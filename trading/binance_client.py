import os

from binance.client import Client
from dotenv import load_dotenv

load_dotenv()


class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")
        self.symbol = os.getenv("TRADE_SYMBOL")
        trade_quantity = os.getenv("TRADE_QUANTITY")
        if trade_quantity is None:
            raise ValueError("TRADE_QUANTITY environment variable is not set.")
        self.quantity = float(trade_quantity)
        self.client = Client(self.api_key, self.api_secret)

    def get_price(self) -> float:
        if not self.symbol:
            raise ValueError(
                "Trade symbol is not set. Check your environment variables."
            )

        try:
            ticker = self.client.get_symbol_ticker(symbol=self.symbol)
            price = ticker.get("price")
            if price is None:
                raise ValueError(f"Price not found for symbol {self.symbol}.")
            return float(price)
        except Exception as e:
            raise RuntimeError(f"Failed to fetch price for symbol {self.symbol}: {e}")

    def place_order(self, side: str):
        if side.upper() not in ["BUY", "SELL"]:
            raise ValueError("Invalid order side")
        return self.client.create_order(
            symbol=self.symbol,
            side=side.upper(),
            type="MARKET",
            quantity=self.quantity,
        )
