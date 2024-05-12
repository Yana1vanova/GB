from datetime import datetime

from pydantic import BaseModel


class TransactionCreate(BaseModel):
    id: int
    amount: str
    currency: str
    from_account: str
    to_account: str
    date: datetime = datetime.utcnow()
    type: str
    details: str
    account_id: int

    class Config:
        orm_mode = True
