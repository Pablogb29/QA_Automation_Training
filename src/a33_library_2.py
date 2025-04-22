import datetime as datetime

def library(requests, books):

    results = []
    user_books = {}
    borrowed = {}  

    for i, request in enumerate(requests):

        parts = request.split()
        action = parts[0]

        if action == "borrow":
            if len(parts) != 4:
                return [-(i + 1)]

            user = parts[1]
            book = parts[2]

            if book not in books:
                return [-(i + 1)]

            try:
                date = datetime.strptime(parts[3], "%Y-%m-%d").date()
            except ValueError:
                return [-(i + 1)]

            if book in borrowed:
                return [-(i + 1)]

            if user in user_books and len(user_books[user]) >= 3:
                return [-(i + 1)]

            borrowed[book] = (user, date, False)

            if user not in user_books:
                user_books[user] = []

            user_books[user].append(book)

        if action == "renew":
            if len(parts) != 4:
                return [-(i + 1)]

            user = parts[1]
            book = parts[2]

            try:
                date = datetime.strptime(parts[3], "%Y-%m-%d").date()
            except ValueError:
                return [-(i + 1)]

            if book not in borrowed:
                return [-(i + 1)]

            user_existing, old_date, renewed = borrowed[book]

            if user_existing != user:
                return [-(i + 1)]

            if renewed:
                return [-(i + 1)]

            borrowed[book] = (user, date, True)

        if action == "return":
            if len(parts) != 3:
                return [-(i + 1)]

            user = parts[1]
            book = parts[2]

            if book not in borrowed or book not in books:
                return [-(i + 1)]

            user_existing, _, _ = borrowed[book]

            if user_existing != user:
                return [-(i + 1)]

            del borrowed[book]

            if user in user_books and book in user_books[user]:
                user_books[user].remove(book)

        if action == "status":
            if len(parts) != 2:
                return [-(i + 1)]

            book = parts[1]

            if book not in books:
                return [-(i + 1)]

            if book in borrowed:
                results.append("borrowed")
            else:
                results.append("available")

    return results
