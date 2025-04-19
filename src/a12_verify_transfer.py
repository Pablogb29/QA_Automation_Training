def verify_transfer(iban, swift):
    errors = []

    # Validate IBAN
    iban = iban.replace(" ", "").upper()
    if len(iban) < 15 or len(iban) > 34:
        errors.append("Invalid IBAN")
    else:
        reordered_iban = iban[4:] + iban[:4]
        converted_iban = ""
        for char in reordered_iban:
            converted_iban += str(ord(char) - 55) if char.isalpha() else char
        if not converted_iban or int(converted_iban) % 97 != 1:
            errors.append("Invalid IBAN")

    # Validate SWIFT
    swift = swift.replace(" ", "").upper()
    if len(swift) not in [8, 11] or not swift.isalnum():
        errors.append("Malformed SWIFT code")
    else:
        if (
            not swift[:4].isalpha() or
            not swift[4:6].isalpha() or
            not swift[6:8].isalnum()
        ):
            errors.append("Malformed SWIFT code")
        elif len(swift) == 11 and not swift[8:].isalnum():
            errors.append("Malformed SWIFT code")

    return errors if errors else "Transfer verified"
