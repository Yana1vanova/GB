from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from auth.base_config import current_user
from bank_account.models import bank_account, BankAccount
from bank_account.schemas import BankAccountCreate
from database import get_async_session


router = APIRouter(
    prefix="/bank_account",
    tags=["Bank account"]
)


@router.post("/")
async def create_new(new_account: BankAccountCreate, session: AsyncSession = Depends(get_async_session),
                     User = Depends(current_user)):
    stmt = insert(bank_account).values(**new_account.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.get("/by_account_id")
async def get_account_details(account_id: int, session: AsyncSession = Depends(get_async_session),
                              User = Depends(current_user)):
    try:
        query = select(bank_account).where(bank_account.c.id == account_id)
        result = await session.execute(query)
        return result.mappings().all()
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.get("/by_user_id")
async def get_account_details(user_id: int, session: AsyncSession = Depends(get_async_session),
                              User = Depends(current_user)):
    try:
        query = select(bank_account).where(bank_account.c.user_id == user_id)
        result = await session.execute(query)
        return result.mappings().all()
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })



@router.get("/balance")
async def get_account_balance(account_id: int, session: AsyncSession = Depends(get_async_session),
                              User = Depends(current_user)):
    try:
        account = await session.get(BankAccount, account_id)
        return float(account.amount)
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.put("/{account_id}")
async def change_account_details(account_id: int, new_account: BankAccountCreate,
                                 session: AsyncSession = Depends(get_async_session), User = Depends(current_user)):
    try:
        stmt = update(bank_account).where(bank_account.c.id == account_id).values(**new_account.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })



@router.put("/change_balance/{id}")
async def put_new_balance(id: int, new_balance: float, session: AsyncSession = Depends(get_async_session),
                          User = Depends(current_user)):
    try:
        account = await session.get(BankAccount, id)
        account.amount = new_balance
        await session.commit()
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })



@router.delete("/{account_id}")
async def delete_account(account_id: int, new_account: BankAccountCreate,
                                 session: AsyncSession = Depends(get_async_session), User = Depends(current_user)):
    try:
        stmt = delete(bank_account).where(bank_account.c.id == account_id).values(**new_account.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "success"}
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })





