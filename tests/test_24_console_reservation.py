from src.a24_console_reservation import console_reservation

def test_console_reservation():
    consoles = ["PS5", "Xbox", "Switch"]
    requests = [
        "reserve 1 PS5 2024-08-01",
        "reserve 2 PS5 2024-08-01",    # ❌ ya reservada
        "check PS5 2024-08-01",        # → booked
        "cancel 1 PS5",
        "check PS5 2024-08-01",        # → available
        "reserve 3 PS5 2024-08-01",    # ✅ ahora sí
    ]
