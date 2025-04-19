def validate_dni(dni):
    letters = "TRWAGMYFPDXBNJZSQVHLCKE"

    if len(dni) != 9:
        return "Invalid DNI"

    number = dni[:8]
    letter = dni[8].upper()

    if not number.isdigit() or not letter.isalpha():
        return "Invalid DNI"

    index = int(number) % 23
    correct_letter = letters[index]

    if letter == correct_letter:
        return "Valid DNI"
    else:
        return "Invalid DNI"
