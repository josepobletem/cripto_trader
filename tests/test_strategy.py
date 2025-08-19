from trading.strategy import TradingStrategy


def test_should_buy():
    strategy = TradingStrategy()
    short_ema = 105
    long_ema = 100
    assert strategy.should_buy(short_ema, long_ema) is True


def test_should_sell():
    strategy = TradingStrategy()
    short_ema = 95
    long_ema = 100
    assert strategy.should_sell(short_ema, long_ema) is True


def test_decide():
    strategy = TradingStrategy(short_window=3, long_window=5)
    prices = [100, 101, 102, 103, 104]
    for price in prices:
        strategy.decide(price)
    decision = strategy.decide(105)
    assert decision == "buy"
