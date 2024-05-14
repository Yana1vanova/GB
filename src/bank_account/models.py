from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey, Float

from database import metadata, Base

bank_account = Table(
    "bank_account",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("amount", Float, nullable=False),
    Column("currency", String, nullable=False, default='RUB'),
    Column("tariff", String, default='default'),
    Column("type", String, default='debit'),
    Column("user_id", Integer, ForeignKey("user.id")),

)


class BankAccount(Base):
    __tablename__ = "bank_account"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    currency = Column(String, nullable=False, default='RUB'),
    tariff = Column(String, default='default'),
    date = Column(TIMESTAMP, default=datetime.utcnow),
    type = Column(String, default='debit'),
    user_id = Column(Integer, ForeignKey("user.id")),
