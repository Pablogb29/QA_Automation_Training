from src.a34_logistic_control import logistic_control

def test_logistic_control():
    products = ["Widget", "Sprocket", "Gadget"]
    requests = [
    "add Widget 10",
    "add Gadget 5",
    "reserve ORD001 Widget 4",
    "reserve ORD001 Gadget 2",         # ❌ solo hay 5, y ya se reservó 1 → error
    "status Widget",                   # → 6 (10 - 4)
    "confirm ORD001",
    "status Widget",                   # → 6 (confirm doesn't change available)
    "cancel ORD001",                   # ❌ error: ya confirmado
]
