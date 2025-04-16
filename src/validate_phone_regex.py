def validate_phone_regex(number: str) -> bool:
    import re
    patron = r"^\+\d{1,3}\d{7,12}$"
    return bool(re.match(patron, number))

    

