from src.a19_library import library

def test_library():
    books = {
    "1984": 2,
    "Dune": 1,
    "Hamlet": 3
}

requests = [
    "borrow 1 Dune",
    "borrow 2 1984",
    "borrow 3 Dune",      # ❌ no disponible
    "inventory",
    "return 1 Dune",
    "inventory"
]
