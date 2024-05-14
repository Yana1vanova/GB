from httpx import AsyncClient


async def test_create_new_account(ac: AsyncClient):
    response = await ac.post("/bank_account/", json={
        "id": 1,
        "amount": 1,
        "user_id": 1
    })
    assert response.status_code == 200


async def test_get_account_by_id(ac: AsyncClient):
    response = await ac.get("/bank_account/by_account_id?account_id=1")
    assert response.status_code == 200
    assert response.json()[0]['id'] == 1
    assert response.json()[0]['amount'] == 1
    assert response.json()[0]['user_id'] == 1


async def test_get_account_by_user(ac: AsyncClient):
    response = await ac.get("/bank_account/by_user_id?user_id=1")
    assert response.status_code == 200
    assert response.json()[0]['id'] == 1
    assert response.json()[0]['type'] == 'debit'
    assert response.json()[0]['currency'] == 'RUB'
    assert response.json()[0]['user_id'] == 1


async def test_get_account_balance(ac: AsyncClient):
    response = await ac.get("/bank_account/balance?account_id=1")
    assert response.status_code == 200
    assert response.text == '1.0'
