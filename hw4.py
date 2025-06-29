import datetime

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Olena Karlovska", "birthday": "1985.12.03"},
    {"name": "Artur Karlovskyi", "birthday": "2004.07.05"},
]

def get_upcoming_birthdays(users):
    today = datetime.date.today()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday < 7:
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() == 5:  # Субота
                congratulation_date += datetime.timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # Неділя
                congratulation_date += datetime.timedelta(days=1)

            congratulation_date_str = congratulation_date.strftime("%Y.%m.%d")
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })

    return upcoming_birthdays

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

