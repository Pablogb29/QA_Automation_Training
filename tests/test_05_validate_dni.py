import src.a05_validate_dni as a05_validate_dni

def test_validate_dni():
    assert a05_validate_dni.validate_dni("12345678Z") == "Valid DNI"
    assert a05_validate_dni.validate_dni("12345678A") == "Invalid DNI"  # Wrong letter
    assert a05_validate_dni.validate_dni("1234567Z") == "Invalid DNI"   # Too short
    assert a05_validate_dni.validate_dni("123456789") == "Invalid DNI"  # No letter
    assert a05_validate_dni.validate_dni("abcdefghI") == "Invalid DNI"  # Not digits
    assert a05_validate_dni.validate_dni("12345678!") == "Invalid DNI"  # Invalid character
