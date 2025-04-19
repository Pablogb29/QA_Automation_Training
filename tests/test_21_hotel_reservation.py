from src.a21_hotel_reservation import hotel_reservation

def test_hotel_reservation():
    rooms = {
    "101": 1,
    "102": 1,
    "103": 1
    }
    requests = [
        "checkin 1 101",
        "checkin 2 102",
        "checkin 3 101",       # ❌ ya está ocupada
        "available",
        "checkout 1 101",
        "available",
        "checkout 3 102"       # ❌ el user 3 no estaba ahí
    ]
