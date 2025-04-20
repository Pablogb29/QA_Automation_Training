import datetime as datetime

def rent_chair(requests, chairs):

    results = []
    rented = {chair:[] for chair in chairs}

    for i, request in enumerate(requests):

        parts = request.split()
        action = parts[0]

        if action == "rent":
            if len(parts) != 4:
                return [-(i+1)]
            
            user = parts[1]
            chair = parts[2]

            if chair not in chairs:
                return [-(i+1)]
            
            try:
                date = datetime.strptime(parts[3], "%Y-%m-%d").date()
            except ValueError:
                return [-(i+1)]
            
            for user_existing, date_existing in rented[chair]:
                if date_existing == date:
                    return [-(i+1)]

            rented[chair].append((user,date))

        if action == "check":
            if len(parts) != 3:
                return [-(i+1)]

            chair = parts[1]

            try:
                date = datetime.strptime(parts[2], "%Y-%m-%d").date()
            except ValueError:
                return [-(i+1)]
            
            for _, date_existing in rented[chair]:
                if date_existing == date:
                    results.append("unavailable")
                    break
                else:
                    results.append("available")            

        if action == "return":
            if len(parts) != 3:
                return [-(i+1)]
            
            user = parts[1]
            chair = parts[2]

            if chair not in chairs:
                return [-(i+1)]
            
            found = False
            for j, (user_exisitng,date_existing) in enumerate(rented[chair]):
                if user_exisitng == user:
                    del rented[chair][j]
                    found = True
                    break
            
            if not found:
                return [-(i+1)]
            
            continue
