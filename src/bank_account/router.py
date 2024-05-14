from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from bank_account.models import bank_account, BankAccount
from bank_account.schemas import BankAccountCreate
from database import get_async_session


router = APIRouter(
    prefix="/bank_account",
    tags=["Bank account"]
)


@router.post("/")
async def create_new(new_account: BankAccountCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(bank_account).values(**new_account.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/by_account_id")
async def get_account_details(account_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(bank_account).where(bank_account.c.id == account_id)
    result = await session.execute(query)
    return result.mappings().all()


@router.get("/by_user_id")
async def get_account_details(user_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(bank_account).where(bank_account.c.user_id == user_id)
    result = await session.execute(query)
    return result.mappings().all()


@router.get("/balance")
async def get_account_balance(account_id: int, session: AsyncSession = Depends(get_async_session)):
    account = await session.get(BankAccount, account_id)
    return float(account.amount)


@router.put("/{account_id}")
async def change_account_details(account_id: int, new_account: BankAccountCreate,
                                 session: AsyncSession = Depends(get_async_session)):
    stmt = update(bank_account).where(bank_account.c.id == account_id).values(**new_account.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.put("/change_balance/{id}")
async def put_new_balance(id: int, new_balance: float, session: AsyncSession = Depends(get_async_session)):
    account = await session.get(BankAccount, id)
    account.amount = new_balance
    await session.commit()


@router.delete("/{account_id}")
async def delete_account(account_id: int, new_account: BankAccountCreate,
                                 session: AsyncSession = Depends(get_async_session)):
    stmt = delete(bank_account).where(bank_account.c.id == account_id).values(**new_account.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}





