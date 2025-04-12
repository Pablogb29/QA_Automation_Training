import src.validate_dni as validate_dni

def test_validate_dni():
    assert validate_dni.validate_dni("12345678Z") == "Valid DNI"
    assert validate_dni.validate_dni("12345678A") == "Invalid DNI"  # Wrong letter
    assert validate_dni.validate_dni("1234567Z") == "Invalid DNI"   # Too short
    assert validate_dni.validate_dni("123456789") == "Invalid DNI"  # No letter
    assert validate_dni.validate_dni("abcdefghI") == "Invalid DNI"  # Not digits
    assert validate_dni.validate_dni("12345678!") == "Invalid DNI"  # Invalid character
