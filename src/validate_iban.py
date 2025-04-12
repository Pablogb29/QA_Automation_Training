def validate_iban(iban):
    """
    Validates an IBAN (International Bank Account Number).
    
    :param iban: The IBAN to validate.
    :return: True if the IBAN is valid, False otherwise.
    """
    # Remove spaces and convert to uppercase
    iban = iban.replace(" ", "").upper()

    # IBAN length constraints
    if len(iban) < 15 or len(iban) > 34:
        return False

    # Rearrange the IBAN
    iban = iban[4:] + iban[:4]

    # Convert letters to numbers
    iban_numeric = ""
    for char in iban:
        if char.isdigit():
            iban_numeric += char
        else:
            iban_numeric += str(ord(char) - 55)

    # Validate IBAN using mod 97 algorithm
    return int(iban_numeric) % 97 == 1
