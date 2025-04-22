import datetime as datetime

def work_shift(requests, machines):

    results = []
    schedule = {machine:[] for machine in machines}

    for i, request in enumerate(requests):

        parts = request.split()
        action = parts[0]

        if action == "assign":
            if len(parts) != 6:
                return [-(i + 1)]

            worker = parts[1]
            machine = parts[2]

            if machine not in machines:
                return [-(i + 1)]

            try:
                date = datetime.strptime(parts[3], "%Y-%m-%d").date()
                start_hour = datetime.strptime(parts[4], "%H:%M").time()
                end_hour = datetime.strptime(parts[5], "%H:%M").time()
            except ValueError:
                return [-(i + 1)]

            # 1. Verificar si el trabajador ya tiene un turno ese día en cualquier máquina
            for m in machines:
                for w, d, _, _ in schedule[m]:
                    if w == worker and d == date:
                        return [-(i + 1)]  # ya tiene un turno ese día

            # 2. Verificar si hay solapamiento en esta máquina en ese día
            for w, d, start_existing, end_existing in schedule[machine]:
                if d == date:
                    if not (end_hour <= start_existing or start_hour >= end_existing):
                        return [-(i + 1)]  # solapamiento de horario en la máquina

            # 3. Si todo va bien, asignar el turno
            schedule[machine].append((worker, date, start_hour, end_hour))

        if action == "check":
            if len(parts) != 4:
                return [-(i+1)]
            
            machine = parts[1]

            if machine not in machines:
                return [-(i+1)]
            
            try:
                date = datetime.strptime(parts[2], "%Y-%m-%d").date()
                hour = datetime.strptime(parts[3], "%H:%M").time()
            except ValueError:
                return [-(i + 1)]
            
            for w,d,start_existing,end_existing in schedule[machine]:
                if d == date:
                    if start_existing <= hour <= end_existing:
                        results.append("unavailable")
                        break
            else:
                results.append("available")
        
        if action == "cancel":
            if len(parts) != 2:
                return [-(i+1)]
            
            worker = parts[1]

            found = False

            for machine in machines:
                for j,(w,_,_,_) in enumerate(schedule[machine]):
                    if w == worker:
                        del schedule[machine][j]
                        found = True
                        break
                if found:
                    break

            if not found:
                return [-(i+1)]
    
    return results