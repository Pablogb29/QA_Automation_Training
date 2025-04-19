from src.a20_rent_car import rent_car

def test_rent_car():
    vehicles = {
    "Tesla": 2,
    "BMW": 1,
    "Toyota": 3
}
requests = [
    "rent 1 Tesla",
    "rent 2 BMW",
    "rent 3 BMW",         # ❌ No disponible
    "return 1 Tesla",
    "status",
    "return 3 BMW",       # ❌ Usuario no tenía ese vehículo
    "status"
]
