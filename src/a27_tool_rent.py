import datetime as datetime

def tool_rent(requests, tools):

    results = []
    rented = {tool:[] for tool in tools}

    for i, request in enumerate(requests):

        parts = request.split()
        action = parts[0]

        if action == "borrow":
            if len(parts) != 4:
                return [-(i+1)]
            
            worker = parts[1]
            tool = parts[2]

            if tool not in tools:
                return [-(i+1)]
            
            try:
                date = datetime.strptime(parts[3], "%Y-%m-%d").date()
            except ValueError:
                return [-(i+1)]
            
            for worker_existing, date_existing in rented[tool]:
                if date == date_existing:
                    return [-(i+1)]

            rented[tool].append((worker,date))
        
        if action == "check":
            if len(parts) != 3:
                return [-(i+1)]
            
            tool = parts[1]

            if tool not in tools:
                return [-(i+1)]
            
            try:
                date = datetime.strptime(parts[2], "%Y-%m-%d").date()
            except ValueError:
                return [-(i+1)]

            for worker_existing, date_existing in rented[tool]:
                if date == date_existing:
                    results.append("unavailable")
                    break    
            else:
                results.append("available") 
    
        if action == "return":
            if len(parts) != 3:
                return [-(i+1)]
            
            worker = parts[1]
            tool = parts[2]

            if tool not in tools:
                return [-(i+1)]
            
            found = False
            for j,(worker_existing,_) in enumerate(rented[tool]):
                if worker_existing == worker:
                    del rented[tool][j]
                    found = True
                    break
            if not found:
                return [-(i+1)]
                
    return results