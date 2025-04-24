import datetime as datetime

def project_manager(requests):
    
    results = []
    projects = {}

    for i, request in enumerate(requests):

        parts = request.split()
        action = parts[0]

        if action == "create":
            if len(parts) != 2:
                return [-(i+1)]
            
            project = parts[1]

            if project in projects:
                return [-(i+1)]
            
            projects[project] = {
                "tasks": {}
            }

        if action == "add_task":
            if len(parts) != 3:
                return [-(i+1)]
            
            project = parts[1]
            task = parts[2]

            if project not in projects:
                return [-(i+1)]
            
            if task in projects[project]["tasks"]:
                return [-(i+1)]
            
            projects[project]["tasks"][task] = {
                "done": False,
                "depends_on": []
            }

        if action == "add_dependency":
            if len(parts) != 4:
                return [-(i+1)]
            
            project = parts[1]
            task = parts[2]
            dependency = parts[3]

            if project not in projects:
                return [-(i+1)]
            
            if task not in projects[project]["tasks"]:
                return [-(i+1)]
            
            if dependency not in projects[project]["tasks"]:
                return [-(i + 1)] 

            if dependency not in projects[project]["tasks"][task]["depends_on"]:
                projects[project]["tasks"][task]["depends_on"].append(dependency)

        if action == "complete":
            if len(parts) != 3:
                return [-(i + 1)]

            project = parts[1]
            task = parts[2]

            if project not in projects:
                return [-(i + 1)]

            if task not in projects[project]["tasks"]:
                return [-(i + 1)]

            for dependency in projects[project]["tasks"][task]["depends_on"]:
                if not projects[project]["tasks"][dependency]["done"]:
                    return [-(i + 1)]  

            projects[project]["tasks"][task]["done"] = True

        if action == "status":
            if len(parts) != 2:
                return [-(i + 1)]

            project = parts[1]

            if project not in projects:
                return [-(i + 1)]

            for task, info in projects[project]["tasks"].items():
                if info["done"]:
                    results.append("done")
                elif any(not projects[project]["tasks"][dep]["done"] for dep in info["depends_on"]):
                    results.append("blocked")
                else:
                    results.append("pending")

    return results

            