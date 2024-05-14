from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey, Float

from database import metadata, Base

transaction = Table(
    "transaction",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("amount", Float, nullable=False),
    Column("currency", String, nullable=False, default='RUB'),
    Column("to_account", Integer, nullable=False, default=0),
    Column("date", TIMESTAMP, default=datetime.utcnow),
    Column("type", String, default='withdraw'),
    Column("details", String),
    Column("account_id", Integer, ForeignKey("bank_account.id")),

)

class Transaction(Base):
    __tablename__ = "transaction"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    currency = Column(String, nullable=False, default='RUB'),
    to_account = Column(Integer, nullable=False, default=0),
    date = Column(TIMESTAMP, default=datetime.utcnow),
    type = Column(String, default='withdraw'),
    details = Column(String),
    account_id = Column(Integer, ForeignKey("bank_account.id")),

