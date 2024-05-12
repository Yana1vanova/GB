from datetime import datetime

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, ForeignKey

from database import metadata, Base

transaction = Table(
    "transaction",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("amount", String, nullable=False),
    Column("currency", String, nullable=False, default='RUB'),
    Column("from_account", String, nullable=False),
    Column("to_account", String, nullable=False, default='ATM'),
    Column("date", TIMESTAMP, default=datetime.utcnow),
    Column("type", String, default='withdraw'),
    Column("details", String),
    Column("account_id", Integer, ForeignKey("bank_account.id")),

)

class Transaction(Base):
    __tablename__ = "transaction"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    amount = Column(String, nullable=False)
    currency = Column(String, nullable=False, default='RUB'),
    from_account = Column(String, nullable=False),
    to_account = Column(String, nullable=False, default='ATM'),
    date = Column(TIMESTAMP, default=datetime.utcnow),
    type = Column(String, default='withdraw'),
    details = Column(String),
    account_id = Column(Integer, ForeignKey("bank_account.id")),

