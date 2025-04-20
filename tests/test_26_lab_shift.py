from src.a26_lab_shift import lab_shift

def test_lab_shift():
    labs = ["LAB1", "LAB2"]
    requests = [
        "book 1001 LAB1 2024-10-01",
        "book 1002 LAB1 2024-10-01",   # ❌ ya reservado
        "check LAB1 2024-10-01",       # → booked
        "cancel 1001 LAB1",
        "check LAB1 2024-10-01",       # → available
        "book 1002 LAB1 2024-10-01"    # ✅ ahora sí
    ]
