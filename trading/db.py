from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Trade(Base):
    __tablename__ = "trades"
    id = Column(Integer, primary_key=True)
    decision = Column(String)
    price = Column(Float)
    explanation = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)


class DatabaseManager:
    def __init__(self, db_url="sqlite:///trades.db"):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def log_trade(self, decision: str, price: float, explanation: str):
        with self.Session() as session:
            trade = Trade(decision=decision, price=price, explanation=explanation)
            session.add(trade)
            session.commit()

    def get_trades(self):
        with self.Session() as session:
            return session.query(Trade).order_by(Trade.timestamp.desc()).all()
