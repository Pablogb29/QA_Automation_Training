def shared_cart(requests):
    cart = {}          # Diccionario que guarda los productos y sus cantidades
    results = []       # Lista que guarda los resultados de las instrucciones "total"

    for i, request in enumerate(requests):
        parts = request.split()
        action = parts[0]

        # Validar mínimo de longitud para cada acción
        if action == "add" or action == "remove":
            if len(parts) != 4:
                return [-(i + 1)]
            user = parts[1]
            product = parts[2]
            try:
                quantity = int(parts[3])
            except ValueError:
                return [-(i + 1)]

            if quantity <= 0:
                return [-(i + 1)]

            if action == "add":
                cart[product] = cart.get(product, 0) + quantity

            elif action == "remove":
                if product not in cart or cart[product] < quantity:
                    return [-(i + 1)]
                cart[product] -= quantity
                if cart[product] == 0:
                    del cart[product]

        elif action == "total":
            if len(parts) != 2:
                return [-(i + 1)]
            total_quantity = sum(cart.values())
            results.append(total_quantity)

        else:
            return [-(i + 1)]

    return results
