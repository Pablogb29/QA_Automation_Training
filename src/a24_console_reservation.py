import datetime as datetime

def console_reservation(requests, consoles):
    
    results = []
    reservations = {console: [] for console in consoles}

    for i, request in enumerate(requests):

        parts = request.split()
        action = parts[0]

        if action == "reserve":
            if len(parts) != 4:
                return [-(i+1)]

            user = parts[1]
            console = parts[2]

            if console not in consoles:
                return [-(i+1)]
            
            try:
                date = datetime.strptime(parts[3], "%Y-%m-%d").date()
            except ValueError:
                return [-(i+1)]
            
            for user_existing, date_existing in reservations[console]:
                if date_existing == date:
                    return [-(i+1)]
            
            reservations[console].append((user,date))

        if action == "check":
            if len(parts) != 3:
                return [-(i + 1)]

            console = parts[1]

            if console not in consoles:
                return [-(i + 1)]

            try:
                date = datetime.strptime(parts[2], "%Y-%m-%d").date()
            except ValueError:
                return [-(i + 1)]

            # Revisar si la fecha ya está reservada
            for user_existing, date_existing in reservations[console]:
                if date_existing == date:
                    results.append("booked")
                    break
            else:
                results.append("available")

            continue
                
        if action == "cancel":
            if len(parts) != 3:
                return [-(i + 1)]

            user = parts[1]
            console = parts[2]

            if console not in consoles:
                return [-(i + 1)]

            found = False
            for idx, (user_existing, date_existing) in enumerate(reservations[console]):
                if user_existing == user:
                    del reservations[console][idx]
                    found = True
                    break

            if not found:
                return [-(i + 1)]

            continue

