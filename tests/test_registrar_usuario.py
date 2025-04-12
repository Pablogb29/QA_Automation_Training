import pytest
from src.register_user import register_user

@pytest.mark.parametrize("name, email, password, birth_date, dni, expected", [
    # ✅ Fully valid case
    ("Pablo", "pablo@email.com", "Pa$$w0rd123", "1995-05-20", "12345678Z", "Successful registration"),

    # ❌ Invalid email
    ("Pablo", "pabloemail.com", "Pa$$w0rd123", "1995-05-20", "12345678Z", ["Invalid email."]),

    # ❌ Weak password
    ("Pablo", "pablo@email.com", "password", "1995-05-20", "12345678Z", [
        "Password must have at least 8 characters, one uppercase letter, one lowercase letter, one digit, and one special character."
    ]),
    ("Pablo", "pablo@email.com", "Pa$$w0rd123", "no-date", "12345678Z", ["Invalid birth date."]),

    # ❌ Underage
    ("Pablo", "pablo@email.com", "Pa$$w0rd123", "2010-01-01", "12345678Z", ["You must be at least 18 years old to register."]),

    # ❌ DNI with incorrect letter
    ("Pablo", "pablo@email.com", "Pa$$w0rd123", "1995-05-20", "12345678A", ["Incorrect DNI letter."]),

    # ❌ All fields invalid
    ("", "pabloemail", "123", "fecha", "1234", [
        "Name is required.",
        "Invalid email.",
        "Password must have at least 8 characters, one uppercase letter, one lowercase letter, one digit, and one special character.",
        "Invalid birth date.",
        "Invalid DNI format."
    ])
])
def test_register_user(name, email, password, birth_date, dni, expected):
    result = register_user(name, email, password, birth_date, dni)
    assert result == expected
