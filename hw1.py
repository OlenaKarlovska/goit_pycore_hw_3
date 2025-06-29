from datetime import datetime

def get_days_from_today(date:str) -> int:
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        diff = today - date
        return diff.days
    except ValueError:
        return ValueError("Невірний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")

test_date = '2025-5-20'
result = get_days_from_today(test_date)
print(f"Кількість днів від {test_date} до сьогодні: {result}")