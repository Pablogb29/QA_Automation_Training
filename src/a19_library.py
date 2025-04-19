def library(requests, books):

    results = []
    borrowed = {}  # Diccionario para saber qué libros tiene cada user

    for i, request in enumerate(requests):
        parts = request.split()
        action = parts[0]

        if action == "inventory":
            total_books = sum(books.values())
            results.append(total_books)
            continue

        user = parts[1]
        book = parts[2]

        if action == "borrow":
            if book not in books or books[book] == 0:
                results = [-(i + 1)]
                break

            books[book] -= 1

            if user not in borrowed:
                borrowed[user] = set()
            borrowed[user].add(book)

        elif action == "return":
            if user not in borrowed or book not in borrowed[user]:
                results = [-(i + 1)]
                break

            books[book] += 1
            borrowed[user].remove(book)
            if not borrowed[user]:
                del borrowed[user]

        else:
            results = [-(i + 1)]
            break

    results

