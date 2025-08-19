import os

import pytest

from trading.db import DatabaseManager
from trading.strategy import TradingStrategy


@pytest.fixture
def strategy():
    return TradingStrategy()


@pytest.fixture
def test_db():
    db = DatabaseManager(db_url="sqlite:///test_trades.db")
    yield db
    os.remove("test_trades.db")
