import src.filter_valid_transactions as filter_valid_transactions

def test_filter_valid_transactions():
    transactions = [
        {'amount': 100, 'currency': 'USD', 'status': 'completed'},
        {'amount': -50, 'currency': 'EUR', 'status': 'completed'},
        {'amount': 200, 'currency': 'JPY', 'status': 'completed'},
        {'amount': 0, 'currency': 'USD', 'status': 'completed'},
        {'amount': 150, 'currency': 'GBP', 'status': 'completed'}
    ]

    expected_valid_transactions = [
        {'amount': 100, 'currency': 'USD', 'status': 'completed'},
        {'amount': 200, 'currency': 'JPY', 'status': 'completed'}
    ]

    assert filter_valid_transactions.filter_valid_transactions(transactions) == expected_valid_transactions
