from src.a32_work_shifts import work_shift

def test_work_shift():
    machines = ["M1", "M2", "M3"]
    requests = [
    "assign w1 M1 2024-11-01 06:00 14:00",
    "assign w1 M2 2024-11-01 14:00 22:00",   # ❌ ya tiene un turno ese día
    "assign w2 M1 2024-11-01 13:00 18:00",   # ❌ máquina solapada
    "check M1 2024-11-01 07:30",             # → occupied
    "check M2 2024-11-01 07:30",             # → free
    "cancel w1",
    "check M1 2024-11-01 07:30"              # → free
]
