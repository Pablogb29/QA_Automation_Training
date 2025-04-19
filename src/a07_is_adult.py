from datetime import datetime

def is_adult(date_str):
  
    try:
        birth_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return False

    current_date = datetime.now()
    difference = current_date - birth_date

    return difference.days >= 6570
