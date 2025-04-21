import datetime as datetime

def booking(requests, rooms):

    results = []
    rented = {room:[] for room in rooms}

    for i, request in enumerate(requests):

        parts = request.split()
        action = parts[0]

        if action == "reserve":
            if len(parts) != 5:
                return [-(i+1)]
            
            user = parts[1]
            room = parts[2]

            if room not in rooms:
                return [-(i+1)]

            try:
                start_date = datetime.strptime(parts[3], "%Y-%m-%d").date()
            except ValueError:
                return [-(i+1)]
            
            try:
                end_date = datetime.strptime(parts[4], "%Y-%m-%d").date()
            except ValueError:
                return [-(i+1)]

            for _, existing_start, existing_end in rented[room]:
                if not (end_date < existing_start or start_date > existing_end):
                    return [-(i+1)]

                
            rented[room].append((user,start_date, end_date))
        
        if action == "check":
            if len(parts) != 3:
                return [-(i+1)]
            
            room = parts[1]
            
            if room not in rooms:
                return [-(i+1)]
            
            try:
                date = datetime.strptime(parts[2], "%Y-%m-%d").date()
            except ValueError:
                return [-(i+1)]
            
            for _, existing_start, existing_end in rented[room]:
                if (existing_start <= date <= existing_end):
                    results.append("unavailable")
                    break
            else:
                results.append("available")

        if action == "cancel":
            if len(parts) != 3:
                return [-(i+1)]
            
            user = parts[1]
            room = parts[2]

            if room not in rooms:
                return [-(i+1)]
            
            found = False
            for j, (user_existing,_,_) in rented[room]:
                if user_existing == user:
                    del rented[room][j]
                    found = True
                    break
            if not found:
                return [-(i+1)]
            
    return results