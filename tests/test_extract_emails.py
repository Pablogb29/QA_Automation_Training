from src.extract_emails import extract_emails

def test_extract_emails():
    text = """
        Some emails: test@email.com, invalid@, john.doe@email.co.uk,
        hello@domain, .bad@email.com, valid@domain.es
        Also: weird@company.travel and another_invalid@domain
    """
    result = extract_emails(text)
    assert "test@email.com" in result
    assert "john.doe@email.co.uk" in result
    assert "valid@domain.es" in result
    assert "weird@company.travel" in result
    assert "invalid@" not in result
    assert ".bad@email.com" not in result
    assert "hello@domain" not in result
    assert "another_invalid@domain" not in result
