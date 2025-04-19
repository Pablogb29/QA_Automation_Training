from datetime import datetime

def package_delivery(requests, packages):

    results = []
    deliveries = {}

    for i, request in enumerate(requests):
        parts = request.split()
        action = parts[0]

        if action == "status":
            if len(parts) != 3:
                return [-(i + 1)]

            package = parts[1]

            if package not in packages:
                return [-(i + 1)]

            try:
                requested_date = datetime.strptime(parts[2], "%Y-%m-%d").date()
            except ValueError:
                return [-(i + 1)]

            if package not in deliveries:
                return [-(i + 1)]

            delivery = deliveries[package]
            if delivery["date"] != requested_date:
                return [-(i + 1)]

            results.append("delivered" if delivery["status"] == "delivered" else "pending")
            continue

        if action == "assign":
            if len(parts) != 4:
                return [-(i + 1)]

            worker = parts[1]
            package = parts[2]

            if package not in packages:
                return [-(i + 1)]

            try:
                delivery_date = datetime.strptime(parts[3], "%Y-%m-%d").date()
            except ValueError:
                return [-(i + 1)]

            if package in deliveries:
                return [-(i + 1)]

            deliveries[package] = {
                "worker": worker,
                "date": delivery_date,
                "status": "pending"
            }

            continue

        if action == "deliver":
            if len(parts) != 3:
                return [-(i + 1)]

            worker = parts[1]
            package = parts[2]

            if package not in packages:
                return [-(i + 1)]

            if package not in deliveries:
                return [-(i + 1)]

            if deliveries[package]["worker"] != worker:
                return [-(i + 1)]

            if deliveries[package]["status"] == "delivered":
                return [-(i + 1)]

            deliveries[package]["status"] = "delivered"
            continue

    return results
