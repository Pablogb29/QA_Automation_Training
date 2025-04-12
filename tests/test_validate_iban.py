import src.validate_iban as validate_iban

def test_validate_iban():
    assert validate_iban.validate_iban("ES7620770024003102575766") == True, "Valid IBAN"
    assert validate_iban.validate_iban("DE89370400440532013000") == True, "Valid IBAN"
    assert validate_iban.validate_iban("123456789012345") == False, "Invalid IBAN"
    assert validate_iban.validate_iban("ES76 2077 0024 0031") == False, "Invalid IBAN"
    assert validate_iban.validate_iban("GB29NWBK60161331926819") == True, "Valid IBAN"
    assert validate_iban.validate_iban("ES76") == False, "Invalid IBAN"
    assert validate_iban.validate_iban("es7620770024003102575766") == True, "Valid IBAN"
