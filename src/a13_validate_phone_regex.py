import re

def validate_phone_regex(number: str) -> bool:
    pattern = r"^\+\d{1,3}\d{7,12}$"
    return bool(re.match(pattern, number))