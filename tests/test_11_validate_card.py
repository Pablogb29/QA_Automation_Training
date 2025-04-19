import src.a11_validate_card as a11_validate_card

def test_validate_card():
    assert a11_validate_card.validate_card("4111111111111111") == "Valid card"
    assert a11_validate_card.validate_card("1234567890123456") == "Invalid card"
    assert a11_validate_card.validate_card("12345678ABCD3456") == "Invalid format"
    assert a11_validate_card.validate_card("4111 1111 1111 1111") == "Valid card"
    assert a11_validate_card.validate_card("411111111111111") == "Invalid format"
