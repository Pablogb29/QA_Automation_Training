import src.is_adult as is_adult

def test_is_adult():
    assert is_adult.is_adult("2000-01-01") == True, "Should be an adult"
    assert is_adult.is_adult("2010-05-20") == False, "Should be a minor"
    assert is_adult.is_adult("2020-12-31") == False, "Should be a minor"
    assert is_adult.is_adult("1990-06-15") == True, "Should be an adult"
    assert is_adult.is_adult("not-a-date") == False, "Invalid date"
    assert is_adult.is_adult("2000/01/01") == False, "Invalid date format"
    assert is_adult.is_adult(" ") == False, "Invalid date string"
