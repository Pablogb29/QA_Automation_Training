from src.a17_verify_user_balance import verify_user_balance

def test_verify_user_balance():

    balances = [100, 200, 300]
    owners = [
        {1, 2},     # Cuenta 0: user 1 y 2
        {2},        # Cuenta 1: user 2
        {3}         # Cuenta 2: user 3
    ]

    requests = [
        "total_balance 2",       # user 2 tiene acceso a cuenta 0 y 1 → 100 + 200 = 300
        "authorize 2 1",         # autoriza al user 1 en cuenta 2
        "deposit 2 1 50",        # user 1 ahora puede depositar en cuenta 2
        "total_balance 1",       # user 1 tiene cuenta 0 y ahora también 2 → 100 + 350 = 450
        "deposit 1 4 50"         # ❌ user 4 no está autorizado en cuenta 1 → devuelve [-5]
    ]
