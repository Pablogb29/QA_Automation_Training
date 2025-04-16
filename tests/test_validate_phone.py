import pytest
import src.validate_phone as validate_phone
import src.validate_phone_regex as validate_phone_regex

@pytest.mark.parametrize("func", [validate_phone.validate_phone, validate_phone_regex.validate_phone_regex])
def test_validate_phone(func):
    assert func("+34699123456") is True
    assert func("+123456789012") is True
    assert func("+49176abc567") is False
    assert func("0034699123456") is False
    assert func("+1") is False
