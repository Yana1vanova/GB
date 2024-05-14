from pydantic import BaseModel


class TransactionCreate(BaseModel):
    id: int
    amount: float
    account_id: int

    '''Закомментированные параметры пока 
    не учавствуют в работе приложения,
    задел на будущее 
    currency: str
    to_account: int
    date: datetime = datetime.utcnow()
    type: str
    details: str'''

    class Config:
        orm_mode = True
