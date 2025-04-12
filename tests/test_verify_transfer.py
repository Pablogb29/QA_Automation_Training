import src.verify_transfer as verify_transfer

def test_verify_transfer():
    assert verify_transfer.verify_transfer("ES7620770024003102575766", "BBVAESMMXXX") == "Transfer verified"
    assert verify_transfer.verify_transfer("123456789012345", "BBVAESMM") == ["Invalid IBAN"]
    assert verify_transfer.verify_transfer("ES7620770024003102575766", "BBV123") == ["Malformed SWIFT code"]
    assert verify_transfer.verify_transfer("", "") == ["Invalid IBAN", "Malformed SWIFT code"]
