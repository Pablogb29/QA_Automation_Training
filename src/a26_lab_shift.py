import datetime as datetime

def lab_shift(requests, labs):

    results = []
    reserved = {lab:[] for lab in labs}

    for i, request in enumerate(requests):
    
        parts = request.split()
        action = parts[0]

        if action == "book":
            if len(parts) != 4:
                return [-(i+1)]
            
            student = parts[1]
            lab = parts[2]

            if lab not in labs:
                return [-(i+1)]
            
            try:
                date = datetime.strptime(parts[3], "%Y-%m-%d").date()
            except ValueError:
                return [-(i+1)]
            
            for user_existing, date_existing in reserved[lab]:
                if date == date_existing:
                    return [-(i+1)]
            
            reserved[lab].append((student,date))

        if action == "check":

            lab = parts[1]

            if lab not in labs:
                return [-(i+1)]
            
            try:
                date = datetime.strptime(parts[2], "%Y-%m-%d").date()
            except ValueError:
                return [-(i+1)]
            
            for user_existing, date_existing in reserved[lab]:
                if date == date_existing:
                    results.append("booked")
                    break
            else: 
                results.append("available")
        
        if action == "cancel":

            student = parts[1]
            lab = parts[2]

            if lab not in labs:
                return [-(i+1)]
            
            found = False
            for j, (user_existing, _) in enumerate(reserved[lab]):
                if user_existing == student:
                    del reserved[lab][j]
                    found = True
                    break
            if not found:
                return [-(i+1)]
                
    print("Final results:", results)

                
