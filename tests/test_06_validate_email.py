import src.a06_validate_email as a06_validate_email

def test_validate_email():
    assert a06_validate_email.validate_email("pablo@email.com") == True, "Valid email"
    assert a06_validate_email.validate_email("pablo@correo.es") == True, "Valid email"
    assert a06_validate_email.validate_email("@domain.com") == False, "Invalid email"
    assert a06_validate_email.validate_email("user@domain") == False, "Invalid email"
    assert a06_validate_email.validate_email("user@.com") == True, "Valid email"
    assert a06_validate_email.validate_email("user@domain.") == False, "Invalid email"
    assert a06_validate_email.validate_email("user domain@correo") == False, "Invalid email"
    assert a06_validate_email.validate_email("user@correo.com") == True, "Valid email"
    assert a06_validate_email.validate_email(" user@correo.com") == False, "Invalid email"
    assert a06_validate_email.validate_email("user@correo..com") == False, "Invalid email"
