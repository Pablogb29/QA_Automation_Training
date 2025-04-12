from datetime import datetime

def valid_date(date_str, start_date, end_date):
    
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return False

    date_start = datetime.strptime(start_date, '%Y-%m-%d')
    date_end = datetime.strptime(end_date, '%Y-%m-%d')

    return date_start <= date <= date_end
