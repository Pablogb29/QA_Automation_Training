import datetime as datetime

def study_room_rent(requests, rooms):

    results = []
    rented = {room:[] for room in rooms}

    for i, request in enumerate(requests):

        parts = request.split()
        action = parts[0]

        if action == "reserve":
            if len(parts) != 4:
                return [-(i+1)]
            
            student = parts[1]
            room = parts[2]

            if room not in rooms:
                return [-(i+1)]

            try:
                date = datetime.strptime(parts[3], "%Y-%m-%d").date()
            except ValueError:
                return [-(i+1)]
            
            for student_existing, date_existing in rented[room]:
                if date_existing == date:
                    return [-(i+1)]
                
            rented[room].append((student,date))
        
        if action == "check":
            if len(parts) != 3:
                return [-(i+1)]
            
            room = parts[1]
            
            try:
                date = datetime.strptime(parts[2], "%Y-%m-%d").date()
            except ValueError:
                return [-(i+1)]
            
            for student_existing, date_existing in rented[room]:
                if date_existing == date:
                    results.append("unavailable")
                    break
            else:
                results.append("available")

        if action == "cancel":
            if len(parts) != 3:
                return [-(i+1)]
            
            student = parts[1]
            room = parts[2]

            if room not in rooms:
                return [-(i+1)]
            
            found = False
            for j, (student_existing,_) in rented[room]:
                if student_existing == student:
                    del rented[room][j]
                    found = True
                    break
            if not found:
                return [-(i+1)]
            
    return results