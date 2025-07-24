def test_should_buy(strategy):
    assert strategy.should_buy(29000) is True
    assert strategy.should_buy(31000) is False

def test_should_sell(strategy):
    assert strategy.should_sell(36000) is True
    assert strategy.should_sell(34000) is False

def test_decide(strategy):
    assert strategy.decide(29000) == "buy"
    assert strategy.decide(36000) == "sell"
    assert strategy.decide(32000) == "hold"
