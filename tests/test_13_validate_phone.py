import pytest
import src.a13_validate_phone as a13_validate_phone
import src.a13_validate_phone_regex as a13_validate_phone_regex

@pytest.mark.parametrize("func", [a13_validate_phone.validate_phone, a13_validate_phone_regex.validate_phone_regex])
def test_validate_phone(func):
    assert func("+34699123456") is True
    assert func("+123456789012") is True
    assert func("+49176abc567") is False
    assert func("0034699123456") is False
    assert func("+1") is False
