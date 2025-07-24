from apscheduler.schedulers.background import BackgroundScheduler
from prometheus_client import Counter
from trading.logger import Logger

TRADE_COUNTER = Counter("trade_decisions_total", "Conteo de decisiones de trade", ["decision"])
ERROR_COUNTER = Counter("trade_errors_total", "Errores durante ejecución")

class TradingScheduler:
    def __init__(self, client, strategy, explainer, db):
        self.client = client
        self.strategy = strategy
        self.explainer = explainer
        self.db = db
        self.logger = Logger()
        self.scheduler = BackgroundScheduler()

    def run_cycle(self):
        try:
            price = self.client.get_price()
            decision = self.strategy.decide(price)
            explanation = self.explainer.explain(decision, price)
            self.logger.log(f"Price: {price}, Decision: {decision}")
            TRADE_COUNTER.labels(decision).inc()
            if decision in ["buy", "sell"]:
                self.client.place_order(decision)
            self.db.log_trade(decision, price, explanation)
        except Exception as e:
            ERROR_COUNTER.inc()
            self.logger.log(f"Error: {str(e)}")

    def start(self):
        self.scheduler.add_job(self.run_cycle, "interval", minutes=5)
        self.scheduler.start()
