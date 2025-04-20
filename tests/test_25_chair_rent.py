from src.a25_chair_rent import rent_chair

def test_rent_chair():
    chairs = ["A", "B", "C"]
    requests = [
    "rent 1 A 2024-09-01",
    "rent 2 A 2024-09-01",    # ❌ ya alquilada
    "check A 2024-09-01",     # → unavailable
    "return 1 A",
    "check A 2024-09-01",     # → available
    "rent 2 A 2024-09-01"     # ✅ ahora sí
]
