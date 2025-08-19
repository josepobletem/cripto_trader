from unittest.mock import MagicMock

from trading.scheduler import TradingScheduler


def test_run_cycle_logs_and_stores():
    client = MagicMock()
    strategy = MagicMock()
    explainer = MagicMock()
    db = MagicMock()
    client.get_price.return_value = 29000.0
    strategy.decide.return_value = "buy"
    explainer.explain.return_value = "Se decidió comprar."
    scheduler = TradingScheduler(client, strategy, explainer, db)
    scheduler.run_cycle()
    client.get_price.assert_called_once()
    strategy.decide.assert_called_once()
    explainer.explain.assert_called_once()
    db.log_trade.assert_called_once_with("buy", 29000.0, "Se decidió comprar.")
