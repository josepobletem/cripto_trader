import pytest
from trading.strategy import TradingStrategy
from trading.db import DatabaseManager
import os

@pytest.fixture
def strategy():
    return TradingStrategy()

@pytest.fixture
def test_db():
    db = DatabaseManager(db_url="sqlite:///test_trades.db")
    yield db
    os.remove("test_trades.db")
