from collections import deque


class TradingStrategy:
    def __init__(self, short_window=3, long_window=5):
        self.prices = deque(maxlen=long_window)
        self.short_window = short_window
        self.long_window = long_window

    def ema(self, prices, span):
        if len(prices) < span:
            return None
        k = 2 / (span + 1)
        ema = prices[0]
        for price in prices[1:]:
            ema = price * k + ema * (1 - k)
        return ema

    def should_buy(self, short_ema, long_ema):
        return short_ema > long_ema

    def should_sell(self, short_ema, long_ema):
        return short_ema < long_ema

    def decide(self, price: float) -> str:
        self.prices.append(price)
        if len(self.prices) < self.long_window:
            return "hold"
        short_ema = self.ema(list(self.prices)[-self.short_window :], self.short_window)
        long_ema = self.ema(list(self.prices), self.long_window)
        if short_ema is None or long_ema is None:
            return "hold"
        if self.should_buy(short_ema, long_ema):
            return "buy"
        if self.should_sell(short_ema, long_ema):
            return "sell"
        return "hold"
