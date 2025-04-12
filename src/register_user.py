from datetime import datetime

def register_user(name, email, password: str, birth_date: str, dni: str):
    errors = []

    if not name:
        errors.append("Name is required.")

    if not email or "@" not in email or "." not in email:
        errors.append("Invalid email.")

    if not password:
        errors.append("Password is required.")
    elif (
        len(password) < 8 or
        not any(c.isupper() for c in password) or
        not any(c.islower() for c in password) or
        not any(c.isdigit() for c in password) or
        not any(not c.isalnum() for c in password)
    ):
        errors.append("Password must have at least 8 characters, one uppercase letter, one lowercase letter, one digit, and one special character.")

    try:
        birth = datetime.strptime(birth_date, "%Y-%m-%d")
        if (datetime.now() - birth).days < 6570:
            errors.append("You must be at least 18 years old to register.")
    except:
        errors.append("Invalid birth date.")

    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    if len(dni) != 9 or not dni[:8].isdigit() or not dni[8].isalpha():
        errors.append("Invalid DNI format.")
    else:
        number = int(dni[:8])
        letter = dni[8].upper()
        if letters[number % 23] != letter:
            errors.append("Incorrect DNI letter.")

    return errors if errors else "Successful registration"
