def validate_card(number: str):
    number = number.replace(" ", "")

    if len(number) != 16 or not number.isdigit():
        return "Invalid format"

    luhn = [int(c) for c in number]

    for i in range(len(luhn) - 2, -1, -2):
        luhn[i] *= 2
        if luhn[i] > 9:
            luhn[i] -= 9

    return "Valid card" if sum(luhn) % 10 == 0 else "Invalid card"
