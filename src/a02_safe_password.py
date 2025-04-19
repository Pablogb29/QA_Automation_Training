def password(password: str) -> str:
    """
    This function takes a password string and returns a safe password string.
    A safe password string is one that contains at least one uppercase letter,
    one lowercase letter, one digit, and one special character.
    """
    # Check if the password is empty
    if not password:
        return "Password cannot be empty"

    # Check if the password meets the criteria
    has_characters = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)


    if not (has_upper and has_lower and has_digit and has_special):
        return "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character"

    return "Password is safe"