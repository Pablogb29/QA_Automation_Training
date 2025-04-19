def rent_car(requests, vehicles):
    results = []
    rented = {}

    for i, request in enumerate(requests):
        parts = request.split()
        action = parts[0]

        if action == "status":
            available_cars = sum(vehicles.values())
            results.append(available_cars)
            continue

        user = parts[1]
        vehicle = parts[2]

        if action == "rent":
            if vehicle not in vehicles or vehicles[vehicle] == 0:
                return [-(i + 1)]
            vehicles[vehicle] -= 1
            if user not in rented:
                rented[user] = set()
            rented[user].add(vehicle)

        elif action == "return":
            if user not in rented or vehicle not in rented[user]:
                return [-(i + 1)]
            vehicles[vehicle] += 1
            rented[user].remove(vehicle)
            if not rented[user]:
                del rented[user]

        else:
            return [-(i + 1)]

    return results
