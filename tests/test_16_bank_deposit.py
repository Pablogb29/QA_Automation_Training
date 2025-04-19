from src.a16_bank_deposit import bank_deposit

def test_bank_deposit():
    balances = [100, 200]

    requests = [
        "authorize 1 3",           # El user 3 ahora puede usar cuenta 1
        "withdraw 1 3 50",         # OK
        "deposit 0 1 100",         # OK
        "withdraw 0 3 10"          # ❌ user 3 no está autorizado en cuenta 0 → debe devolver [-4]
    ]
