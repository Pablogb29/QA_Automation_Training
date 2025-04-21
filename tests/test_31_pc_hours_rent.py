from src.a31_pc_hours_rent import pc_hours_rent

def test_pc_hours_rent():
    pcs = ["PC1", "PC2"]
    requests = [
    "reserve u1 PC1 2024-11-01 14:00 15:00",
    "reserve u2 PC1 2024-11-01 14:30 15:30",   # ❌ solapa
    "check PC1 2024-11-01 14:45",              # → booked
    "cancel u1 PC1",
    "check PC1 2024-11-01 14:45",              # → available
    "reserve u2 PC1 2024-11-01 14:30 15:30"    # ✅ ahora sí
]
