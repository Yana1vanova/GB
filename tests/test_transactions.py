from httpx import AsyncClient


async def test_add_transaction(ac: AsyncClient):
    prev_balance = await ac.get("/bank_account/balance?account_id=1")
    response = await ac.post("/transactions/", json={
        "id": 1,
        "amount": 1,
        "account_id": 1
    })
    balance = await ac.get("/bank_account/balance?account_id=1")
    assert response.status_code == 200
    assert float(prev_balance.text) - 1 == float(balance.text)


async def get_transactions_by_type(ac: AsyncClient):
    response = await ac.get("/transactions/by_type?transaction_type=withdraw", )
    assert response.status_code == 200
    assert response.json()[0]['id'] == 1
    assert response.json()[0]['type'] == 'withdraw'
    assert response.json()[0]['currency'] == 'RUB'
    assert response.json()[0]['account_id'] == 1
