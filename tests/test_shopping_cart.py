from src.shared_cart import shared_cart

def test_shared_cart():
    requests = [
    "add 1 apple 3",
    "add 2 banana 2",
    "remove 1 apple 1",
    "total 2",
    "remove 2 apple 5"  # ❌ inválido: no hay suficientes manzanas
]
