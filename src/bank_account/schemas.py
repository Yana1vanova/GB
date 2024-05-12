from datetime import datetime

from pydantic import BaseModel


class BankAccountCreate(BaseModel):
    id: int
    amount: str
    # currency: str
    # tariff: str
    # date: datetime
    # type: str
    user_id: int

    class Config:
        orm_mode = True


class BankAccountRead(BaseModel):
    id: int
    amount: str
    currency: str
    tariff: str
    date: datetime
    type: str
    user_id: int

