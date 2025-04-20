from src.a28_padel_rent import padel_rent

def test_padel_rent():
    courts = ["Court1", "Court2"]
    requests = [
    "reserve u1 Court1 2024-10-10",
    "reserve u2 Court1 2024-10-10",    # ❌ ya reservada
    "check Court1 2024-10-10",         # → booked
    "cancel u1 Court1",
    "check Court1 2024-10-10",         # → available
    "reserve u2 Court1 2024-10-10"     # ✅ ahora sí
]
