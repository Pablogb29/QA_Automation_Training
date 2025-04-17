def verify_user_balance(balances, owners, requests):

    results = []
    owners = [{i + 1} for i in range(len(balances))]

    for i, request in enumerate(requests):
        parts = request.split()
        action = parts[0]
        account = int(parts[1])
        user = int(parts[2])

        if account < 0 or account >= len(balances):
            return [-(i + 1)]

        if action == "authorize":
            owners[account].add(user)

        elif action == "deposit":
            amount = int(parts[3])
            balances[account] += amount

        elif action == "withdraw":
            amount = int(parts[3])
            if user not in owners[account]:
                return [-(i + 1)]
            if balances[account] < amount:
                return [-(i + 1)]
            balances[account] -= amount

        elif action == "total_balance":
            total = 0
            for j, owner in enumerate(owners):
                if user in owner:
                    total += balances[j]
                else:
                    return False
        results.append(total)

    return results