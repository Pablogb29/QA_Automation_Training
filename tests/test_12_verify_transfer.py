import src.a12_verify_transfer as a12_verify_transfer

def test_verify_transfer():
    assert a12_verify_transfer.verify_transfer("ES7620770024003102575766", "BBVAESMMXXX") == "Transfer verified"
    assert a12_verify_transfer.verify_transfer("123456789012345", "BBVAESMM") == ["Invalid IBAN"]
    assert a12_verify_transfer.verify_transfer("ES7620770024003102575766", "BBV123") == ["Malformed SWIFT code"]
    assert a12_verify_transfer.verify_transfer("", "") == ["Invalid IBAN", "Malformed SWIFT code"]
