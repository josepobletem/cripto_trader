from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TradeBase(BaseModel):
    decision: str
    price: float
    explanation: str


class TradeOut(TradeBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True


class WebhookRequest(BaseModel):
    trigger: Optional[str] = "manual"
