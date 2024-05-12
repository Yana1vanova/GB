from fastapi import FastAPI

from auth.base_config import auth_backend, fastapi_users
from auth.schemas import UserRead, UserCreate

from transactions.router import router as router_transaction
from thing.router import router as router_thing
from bank_account.router import router as router_bank_account

app = FastAPI(
    title="Trading App"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_transaction)
app.include_router(router_thing)
app.include_router(router_bank_account)

# from datetime import datetime
# from enum import Enum
# from typing import List, Optional
#
# from fastapi_users import FastAPIUsers
# from pydantic import BaseModel, Field, ValidationError
#
# from fastapi import FastAPI, Request, status, Depends
# from fastapi.encoders import jsonable_encoder
# from fastapi.responses import JSONResponse
#
# from auth.base_config import auth_backend
# from auth.manager import get_user_manager
# from auth.schemas import UserRead, UserCreate
#
#
# app = FastAPI(
#     title="Online Bank App"
# )
#
# app.include_router(
#     fastapi_users.get_auth_router(auth_backend),
#     prefix="/auth",
#     tags=["Auth"],
# )
#
# app.include_router(
#     fastapi_users.get_register_router(UserRead, UserCreate),
#     prefix="/auth",
#     tags=["Auth"],
# )
#
# app.include_router(router_operation)
#
# @app.get("/protected-route")
# def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.username}"
#
#
#
# @app.get("/unprotected-route")
# def unprotected_route():
#     return f"Hello, anonym"
#
#
# # Благодаря этой функции клиент видит ошибки, происходящие на сервере, вместо "Internal server error"
# @app.exception_handler(ValidationError)
# async def validation_exception_handler(request: Request, exc: ValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"detail": exc.errors()}),
#     )
#
#
# fake_users = [
#     {"id": 1, "role": "admin", "name": ["Bob"]},
#     {"id": 2, "role": "investor", "name": "John"},
#     {"id": 3, "role": "trader", "name": "Matt"},
#     {"id": 4, "role": "investor", "name": "Homer", "degree": [
#         {"id": 1, "created_at": "2020-01-01T00:00:00", "type_degree": "expert"}
#     ]},
# ]
#
#
# class DegreeType(Enum):
#     newbie = "newbie"
#     expert = "expert"
#
#
# class Degree(BaseModel):
#     id: int
#     created_at: datetime
#     type_degree: DegreeType
#
#
# class User(BaseModel):
#     id: int
#     role: str
#     name: str
#     degree: Optional[List[Degree]] = []
#
#
# @app.get("/users/{user_id}", response_model=List[User])
# def get_user(user_id: int):
#     return [user for user in fake_users if user.get("id") == user_id]
#
#
# fake_trades = [
#     {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
#     {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
# ]
#
#
# class Trade(BaseModel):
#     id: int
#     user_id: int
#     currency: str = Field(max_length=5)
#     side: str
#     price: float = Field(ge=0)
#     amount: float
#
#
# @app.post("/trades")
# def add_trades(trades: List[Trade]):
#     fake_trades.extend(trades)
#     return {"status": 200, "data": fake_trades}
#
#
# @app.get("/")
# def enter_menu():
#     options = {
#         "1": "Зарегистрироваться",
#         "2": "Войти"
#     }
#     return options
#
#
# @app.get("/menu")
# def app_menu():
#     options = {
#         "1": "Открыть счет",
#         "2": "Пополнить счет",
#         "3": "Снять средства",
#         "4": "Сделать перевод",
#         "5": "Узнать баланс",
#         "6": "Вывести информацию об открытых счетах",
#         "7": "Вывести историю операций"
#     }
#     return options
#
#
# @app.post("/menu/{option_number}")
# def choose_app_menu_option(option_number: int):
#     return f"/menu/{app_menu()[f'{option_number}']}"
