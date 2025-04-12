import pytest
from src.classify_age import classify_age

@pytest.mark.parametrize("age, expected", [
    (10, "Child"),
    (15, "Teenager"),
    (30, "Adult"),
    (70, "Elder"),
    (-5, "Invalid age"),
    (0, "Child"),
    (30.5, "Invalid age"),
    ("40", "Invalid age"),
    (None, "Invalid age"),
])
def test_classify_age(age, expected):
    assert classify_age(age) == expected

