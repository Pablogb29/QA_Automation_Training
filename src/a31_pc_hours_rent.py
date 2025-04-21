import datetime as datetime

def pc_hours_rent(requests, pcs):

    results = []
    rented = {pc:[] for pc in pcs}

    for i, request in enumerate(requests):

        parts = request.split()
        action = parts[0]

        if action == "reserve":
            if len(parts) != 6:
                return [-(i+1)]

            user = parts[1]
            pc = parts[2]

            if pc not in pcs:
                return [-(i+1)]

            try:
                date = datetime.strptime(parts[3], "%Y-%m-%d").date()
                start = datetime.strptime(parts[4], "%H:%M").time()
                end = datetime.strptime(parts[5], "%H:%M").time()
            except ValueError:
                return [-(i+1)]

            # Límite de 2 reservas por usuario y día
            user_reservations = sum(
                1 for u, d, _, _ in rented[pc] if u == user and d == date
            )
            if user_reservations >= 2:
                return [-(i+1)]

            # Verificar solapamiento solo en reservas del mismo día
            for _, date_existing, start_existing, end_existing in rented[pc]:
                if date_existing == date:
                    if not (end <= start_existing or start >= end_existing):
                        return [-(i+1)]  # hay solapamiento

            rented[pc].append((user, date, start, end))
        
        if action == "check":

            pc = parts[1]

            if pc not in pcs:
                return [-(i+1)]
            
            try:
                date = datetime.strptime(parts[2], "%Y-%m-%d").date()
            except ValueError:
                return [-(i+1)]

            try:
                time = datetime.strptime(parts[3], "%H:%M").time()
            except ValueError:
                return [-(i+1)]
            
            for _, date_existing, start_existing, end_existing in rented[pc]:
                if date_existing == date:
                    if start_existing <= time <= end_existing:
                        results.append("booked")
                        break
            else:
                results.append("available")


        if action == "cancel":
            if len(parts) != 3:
                return [-(i+1)]
            
            user = parts[1]
            pc = parts[2]

            if pc not in pcs:
                return [-(i+1)]
            
            found = False
            for j,(user_existing,_,_,_) in enumerate(rented[pc]):
                if user_existing == user:
                    del rented[pc][j]
                    found= True
                    break
            else:
                return [-(i+1)]
            
    return results