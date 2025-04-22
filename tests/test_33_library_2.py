from src.a33_library_2 import library

def test_library():
    books = ["Book1", "Book2", "Book3"]
    requests = [
    "borrow u1 Book1 2024-11-01",
    "borrow u2 Book1 2024-11-02",     # ❌ libro ocupado
    "borrow u1 Book2 2024-11-02",
    "renew u1 Book1 2024-11-10",      # ✅
    "renew u1 Book1 2024-11-15",      # ❌ ya renovado
    "return u1 Book1",
    "borrow u2 Book1 2024-11-16",     # ✅ ahora sí
    "status Book1",                   # → borrowed
    "status Book2",                   # → borrowed
    "return u1 Book2",
    "status Book2"                    # → available
]
