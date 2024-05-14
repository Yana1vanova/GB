import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from auth.base_config import current_user
from bank_account.router import put_new_balance, get_account_balance
from database import get_async_session
from transactions.models import transaction
from transactions.schemas import TransactionCreate

router = APIRouter(
    prefix="/transactions",
    tags=["Transaction"]
)


@router.get("/by_type")
async def get_transactions_by_type(transaction_type: str, session: AsyncSession = Depends(get_async_session),
                                   User = Depends(current_user)):
    query = select(transaction).where(transaction.c.type == transaction_type)
    result = await session.execute(query)
    return result.mappings().all()


@router.get("/by_date")
async def get_transactions_by_date(transaction_date: datetime.date, session: AsyncSession = Depends(get_async_session),
                                   User = Depends(current_user)):
    query = select(transaction).where(transaction.c.type.date == transaction_date)
    result = await session.execute(query)
    return result.mappings().all()


@router.post("/")
async def add_transaction(new_transaction: TransactionCreate, session: AsyncSession = Depends(get_async_session),
                          User = Depends(current_user)):
    stmt = insert(transaction).values(**new_transaction.dict())
    account_id = new_transaction.account_id
    balance = await get_account_balance(account_id, session)
    new_balance = balance - new_transaction.amount
    await put_new_balance(account_id, new_balance, session)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.delete("/{account_id}")
async def delete_transaction(transaction_id: int, transaction: TransactionCreate,
                                 session: AsyncSession = Depends(get_async_session), User = Depends(current_user)):
    stmt = delete(transaction).where(transaction.c.id == transaction_id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
