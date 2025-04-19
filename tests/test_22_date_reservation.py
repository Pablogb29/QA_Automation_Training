from src.a22_date_reservation import date_reservation

def tes_date_reservation():
    rooms = ["101", "102", "103"]
    requests = [
        "reserve 1 101 2024-06-01 2024-06-05",
        "reserve 2 101 2024-06-03 2024-06-06",   # ❌ solapa con la anterior
        "availability 101 2024-06-07",          # ✅ libre → results.append("available")
        "cancel 1 101",
        "reserve 2 101 2024-06-03 2024-06-06",   # ✅ ahora sí
        "availability 101 2024-06-04"           # ❌ ocupada → results.append("unavailable")
    ]
