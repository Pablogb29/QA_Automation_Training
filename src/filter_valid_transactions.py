def filter_valid_transactions(transactions):
    
    valid_transactions = []

    for transaction in transactions:
        if (
            transaction.get('amount') > 0 and
            transaction.get('currency') in ['USD', 'EUR', 'JPY'] and
            transaction.get('status') == 'completed'
        ):
            valid_transactions.append(transaction)

    return valid_transactions
