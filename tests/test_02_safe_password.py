import src.a02_safe_password as spw

def test_safe_password():
    # Test with a valid password
    assert spw.password("ValidPassword123!") == "Password is safe"

    # Test with an empty password
    assert spw.password("") == "Password cannot be empty"

    # Test with a password that is too short
    assert spw.password("short") == "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character"

    # Test with a password that has no uppercase letters
    assert spw.password("lowercase123!") == "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character"

    # Test with a password that has no lowercase letters
    assert spw.password("UPPERCASE123!") == "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character"

    # Test with a password that has no digits
    assert spw.password("NoDigits!") == "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character"

    # Test with a password that has no special characters
    assert spw.password("NoSpecialCharacters123") == "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character"