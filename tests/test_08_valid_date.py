import src.a08_valid_date as a08_valid_date

def test_valid_date():
    assert a08_valid_date.valid_date("2025-04-15", "2025-04-01", "2025-04-30") == True, "Valid date"
    assert a08_valid_date.valid_date("2025-03-31", "2025-04-01", "2025-04-30") == False, "Date out of range"
    assert a08_valid_date.valid_date("2025-05-01", "2025-04-01", "2025-04-30") == False, "Date out of range"
    assert a08_valid_date.valid_date("2025-04-01", "2025-04-01", "2025-04-30") == True, "Start boundary valid"
    assert a08_valid_date.valid_date("2025-04-30", "2025-04-01", "2025-04-30") == True, "End boundary valid"
    assert a08_valid_date.valid_date("2025/04/15", "2025-04-01", "2025-04-30") == False, "Invalid date format"
    assert a08_valid_date.valid_date("invalid-date", "2025-04-01", "2025-04-30") == False, "Invalid date string"
    assert a08_valid_date.valid_date("2025-02-31", "2025-04-01", "2025-04-30") == False, "Nonexistent date"
