def hotel_reservation(requests, rooms):
    results = []
    reserved = {}

    for i, request in enumerate(requests):
        parts = request.split()
        action = parts[0]

        if action == "available":
            available_rooms = sum(rooms.values())
            results.append(available_rooms)
            continue  # ✅ seguimos con la siguiente instrucción

        user = parts[1]
        room = parts[2]

        if action == "checkin":
            if room not in rooms or rooms[room] == 0:
                return [-(i + 1)]
            rooms[room] -= 1
            if user not in reserved:
                reserved[user] = set()
            reserved[user].add(room)

        elif action == "checkout":
            if user not in reserved or room not in reserved[user]:
                return [-(i + 1)]
            rooms[room] += 1
            reserved[user].remove(room)
            if not reserved[user]:
                del reserved[user]

        else:
            return [-(i + 1)]

    return results
