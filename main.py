from typing import List

from fastapi import FastAPI, Response
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

from trading.binance_client import BinanceClient
from trading.db import DatabaseManager
from trading.gpt_helper import GPTExplainer
from trading.scheduler import TradingScheduler
from trading.schemas import TradeOut, WebhookRequest
from trading.strategy import TradingStrategy

app = FastAPI(title="Crypto Trader API")

# Inicialización de componentes
client = BinanceClient()
strategy = TradingStrategy()
explainer = GPTExplainer()
db = DatabaseManager()
scheduler = TradingScheduler(client, strategy, explainer, db)
scheduler.start()


@app.get("/")
def home():
    return {"message": "Crypto Trader is running"}


@app.get("/trades", response_model=List[TradeOut])
def get_trades():
    return db.get_trades()


@app.post("/webhook")
async def webhook(payload: WebhookRequest):
    scheduler.run_cycle()
    return {"status": "executed", "trigger": payload.trigger}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
