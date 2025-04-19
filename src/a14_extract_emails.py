def extract_emails(text: str) -> list:
    """
    Extract valid emails from text using basic string logic (no regex).
    """
    words = text.replace(",", " ").replace(";", " ").split()
    valid_emails = []

    for word in words:
        if word.count("@") != 1:
            continue

        local, domain = word.split("@")

        if not local or not domain:
            continue

        if " " in word:
            continue

        if '.' not in domain:
            continue

        if word.startswith("@") or word.endswith("@") or word.startswith(".") or word.endswith("."):
            continue

        valid_emails.append(word)

    return valid_emails
