from src.a23_package_delivery import package_delivery

def test_package_delivery():
    packages = ["PKG001", "PKG002", "PKG003"]
    requests = [
    "assign 1 PKG001 2024-07-01",
    "assign 2 PKG002 2024-07-02",
    "assign 3 PKG001 2024-07-03",    # ❌ ya está asignado
    "deliver 1 PKG001",
    "status PKG001 2024-07-01",      # entregado
    "status PKG002 2024-07-02"       # pendiente
]

