from src.a35_project_manager import project_manager

def test_project_manager():
    requests = [
    "create MyApp",
    "add_task MyApp Design",
    "add_task MyApp Develop",
    "add_dependency MyApp Develop Design",
    "complete MyApp Design",
    "complete MyApp Develop",       # ✅ ahora sí
    "status MyApp"
]
