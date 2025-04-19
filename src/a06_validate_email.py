def validate_email(email):
    if email.count('@') != 1:
        return False

    local_part, domain = email.split('@')

    if not local_part or not domain:
        return False

    if '.' not in domain:
        return False

    if ' ' in email:
        return False

    if '..' in email:
        return False

    if email.startswith('@') or email.endswith('@') or email.startswith('.') or email.endswith('.'):
        return False

    return True
