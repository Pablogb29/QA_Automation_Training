from src.a29_study_room_rent import study_room_rent

def test_study_room_rent():
    rooms = ["Room1", "Room2"]
    requests = [
    "reserve s1 Room1 2024-11-10",
    "reserve s2 Room1 2024-11-10",   # ❌ ya reservada
    "check Room1 2024-11-10",        # → booked
    "cancel s1 Room1",
    "check Room1 2024-11-10",        # → available
    "reserve s2 Room1 2024-11-10"    # ✅ ahora sí
]
