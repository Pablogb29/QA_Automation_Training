from src.a30_booking import booking

def test_booking():
    rooms = ["H1", "H2"]
    requests = [
    "reserve c1 H1 2024-11-01 2024-11-03",
    "reserve c2 H1 2024-11-02 2024-11-04",   # ❌ solapa
    "check H1 2024-11-02",                   # → booked
    "cancel c1 H1",
    "check H1 2024-11-02",                   # → available
    "reserve c2 H1 2024-11-02 2024-11-04"    # ✅ ahora sí
]
