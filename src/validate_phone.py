def validate_phone(number: str) -> bool:
    if not number.startswith("+"):
        return False

    content = number[1:]

    if not content.isdigit():
        return False

    # Try all valid country code splits (1 to 3 digits)
    for i in range(1, 4):
        country_code = content[:i]
        local_number = content[i:]
        if 7 <= len(local_number) <= 12:
            return True

    return False
