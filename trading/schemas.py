from pydantic import BaseModel
from datetime import datetime
from typing import Optional

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
