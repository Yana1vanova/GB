from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean, TIMESTAMP, ForeignKey, JSON

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("hashed_password", String, nullable=False),
    Column("has_agreements", Boolean),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),

)

customer = Table(
    "customer",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False, unique=True),
    Column("name", String, nullable=False),
    Column("address", String, nullable=False),
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("agreement_id", Integer, ForeignKey("agreement.id")),
)

agreement = Table(
    "agreement",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("crated_at", TIMESTAMP, default=datetime.utcnow),
    Column("expire_date", TIMESTAMP),
    Column("file_link", String, nullable=False),
    Column("tariff", String, nullable=False, default='Basic'),
)

account = Table(
    "account",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("number", Integer, nullable=False, unique=True),
    Column("balance", Integer, nullable=False, default=0),
    Column("currency", String, nullable=False, default='RUB'),
    Column("tariff", String, nullable=False, default='Basic'),
    Column("agreement_id", Integer, ForeignKey("agreement.id")),
)