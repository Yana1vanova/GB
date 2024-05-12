import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from transactions.models import transaction
from transactions.schemas import TransactionCreate

router = APIRouter(
    prefix="/transactions",
    tags=["Transaction"]
)


@router.get("/by_type")
async def get_transactions_by_type(transaction_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(transaction).where(transaction.c.type == transaction_type)
    result = await session.execute(query)
    return result.mappings().all()


@router.get("/by_date")
async def get_transactions_by_date(transaction_date: datetime.date, session: AsyncSession = Depends(get_async_session)):
    query = select(transaction).where(transaction.c.type.date == transaction_date)
    result = await session.execute(query)
    return result.mappings().all()


@router.post("/")
async def add_transaction(new_transaction: TransactionCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(transaction).values(**new_transaction.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router.put("/{account_id}")
async def change_account_details(account_id: int, new_account: TransactionCreate,
                                 session: AsyncSession = Depends(get_async_session)):
    stmt = update(transaction).where(transaction.c.id == account_id).values(**new_account.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.delete("/{account_id}")
async def delete_account(account_id: int, new_account: TransactionCreate,
                                 session: AsyncSession = Depends(get_async_session)):
    stmt = delete(transaction).where(transaction.c.id == account_id).values(**new_account.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
