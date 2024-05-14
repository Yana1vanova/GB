from datetime import datetime

from pydantic import BaseModel


class BankAccountCreate(BaseModel):
    id: int
    amount: float
    user_id: int

    '''Закомментированные параметры пока 
    не учавствуют в работе приложения,
    задел на будущее 
    currency: str
    tariff: str
    date: datetime
    type: str
    '''

    class Config:
        orm_mode = True


class BankAccountRead(BaseModel):
    id: int
    amount: float
    currency: str
    tariff: str
    date: datetime
    type: str
    user_id: int

