from datetime import datetime

def date_reservation(requests, rooms):
    results = []
    reservations = {room: [] for room in rooms}

    for i, request in enumerate(requests):
        parts = request.split()
        action = parts[0]

        if action == "availability":
            if len(parts) != 3:
                return [-(i + 1)]
            room = parts[1]
            if room not in rooms:
                return [-(i + 1)]
            try:
                date_request = datetime.strptime(parts[2], "%Y-%m-%d").date()
            except ValueError:
                return [-(i + 1)]

            reserved = False
            for user, start, end in reservations[room]:
                if start <= date_request <= end:
                    reserved = True
                    break

            results.append("unavailable" if reserved else "available")
            continue

        elif action == "reserve":
            if len(parts) != 5:
                return [-(i + 1)]
            user = parts[1]
            room = parts[2]
            if room not in rooms:
                return [-(i + 1)]
            try:
                start = datetime.strptime(parts[3], "%Y-%m-%d").date()
                end = datetime.strptime(parts[4], "%Y-%m-%d").date()
            except ValueError:
                return [-(i + 1)]
            if start > end:
                return [-(i + 1)]

            for _, start_existing, end_existing in reservations[room]:
                if not (end < start_existing or start > end_existing):
                    return [-(i + 1)]

            reservations[room].append((user, start, end))

        elif action == "cancel":
            if len(parts) != 3:
                return [-(i + 1)]
            user = parts[1]
            room = parts[2]
            if room not in rooms:
                return [-(i + 1)]
            found = False
            for idx, (u, start, end) in enumerate(reservations[room]):
                if u == user:
                    del reservations[room][idx]
                    found = True
                    break
            if not found:
                return [-(i + 1)]

        else:
            return [-(i + 1)]

    return results

