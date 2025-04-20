import datetime as datetime

def padel_rent(requests, courts):

    results = []
    rented = {court:[] for court in courts}

    for i, request in enumerate(requests):

        parts = request.split()
        action = parts[0]

        if action == "reserve":
            if len(parts) != 4:
                return [-(i+1)]
            
            user = parts[1]
            court = parts[2]

            if court not in courts:
                return [-(i+1)]
            
            try:
                date = datetime.strptime(parts[3], "%Y-%m-%d").date()
            except ValueError:
                return [-(i+1)]
            
            for user_existing, date_existing in rented[court]:
                if date_existing == date:
                    return [-(i+1)]

            rented[court].append((user,date))
            
        if action == "check":

            if len(parts) != 3:
                return [-(i+1)]
            
            court = parts[1]

            if court not in courts:
                return [-(i+1)]

            try:
                date = datetime.strptime(parts[2], "%Y-%m-%d").date()
            except ValueError:
                return [-(i+1)]
            
            for user_existing, date_existing in rented[court]:
                if date_existing == date:
                    results.append("unavailable")
                    break
            else:
                results.append("available")

        if action == "cancel":

            if len(parts) != 3:
                return [-(i+1)]
            
            user = parts[1]
            court = parts[2]
            
            found = False
            for j, (user_existing,_) in rented[court]:
                if user_existing == user:
                    del rented[court][j]
                    found = True
                    break
            if not found:
                return [-(i+1)]

    return results