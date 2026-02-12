from datetime import datetime

def get_days_from_today(date):
    try:
        
        target_date = datetime.strptime(date, '%Y-%m-%d').date()
        
        today = datetime.today().date()
        
        return (today - target_date).days
    except ValueError:
        return "Неправильний формат дати. Використовуйте РРРР-ММ-ДД."
print(get_days_from_today("2021-10-09"))
