from src.a27_tool_rent import tool_rent

def test_tool_rent():
    tools = ["Drill", "Hammer", "Saw"]
    requests = [
    "borrow w1 Drill 2024-10-05",
    "borrow w2 Drill 2024-10-05",   # ❌ ya prestada
    "check Drill 2024-10-05",       # → unavailable
    "return w1 Drill",
    "check Drill 2024-10-05",       # → available
    "borrow w2 Drill 2024-10-05"    # ✅ ahora sí
]
