def validate_phone(number: str) -> bool:
    if not number.startswith("+"):
        return False
    
    contenido = number[1:]
    
    if not contenido.isdigit():
        return False

    # Intentamos todos los posibles splits válidos del código de país (1 a 3 dígitos)
    for i in range(1, 4):
        codigo = contenido[:i]
        resto = contenido[i:]
        if 7 <= len(resto) <= 12:
            return True

    return False


