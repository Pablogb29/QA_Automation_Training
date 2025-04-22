import datetime as datetime

def logistic_control(requests, products):

    results = []
    stock = {}
    reservations = {}
    confirmed_orders = {}

    for i, request in enumerate(requests):

        parts = request.split()
        action = parts[0]

        if action == "add":
            if len(parts) != 3:
                return [-(i + 1)]

            product = parts[1]

            if product not in products:
                return [-(i + 1)]

            try:
                quantity = int(parts[2])
                if quantity <= 0:
                    return [-(i + 1)]
            except ValueError:
                return [-(i + 1)]

            if product not in stock:
                stock[product] = 0

            stock[product] += quantity

        if action == "reserve":
            if len(parts) != 4:
                return [-(i + 1)]

            order = parts[1]
            product = parts[2]

            if product not in products:
                return [-(i + 1)]

            try:
                quantity = int(parts[3])
                if quantity <= 0:
                    return [-(i + 1)]
            except ValueError:
                return [-(i + 1)]

            if product not in stock or stock[product] < quantity:
                return [-(i + 1)]

            # Descontar temporalmente del stock
            stock[product] -= quantity

            # Inicializar la orden si no existe
            if order not in reservations:
                reservations[order] = {}

            # Agregar el producto a la orden
            if product in reservations[order]:
                reservations[order][product] += quantity
            else:
                reservations[order][product] = quantity

        if action == "confirm":
            if len(parts) != 2:
                return [-(i+1)]
            
            order = parts[1]

            if order not in reservations:
                return [-(i+1)]
            
            confirmed_orders.add(order)

        if action == "status":
            if len(parts) != 2:
                return [-(i+1)]
            
            product = parts[1]

            if product not in products:
                return [-(i+1)]
            
            if product not in stock:
                results.append(0)
            else:
                results.append(stock[product])
            
        if action == "cancel":
            if len(parts) != 2:
                return [-(i + 1)]

            order = parts[1]

            if order not in reservations:
                return [-(i + 1)]

            if order in confirmed_orders:
                return [-(i + 1)]

            # Devolver al stock lo reservado
            for product, quantity in reservations[order].items():
                if product in stock:
                    stock[product] += quantity
                else:
                    stock[product] = quantity

            # Eliminar la reserva
            del reservations[order]


