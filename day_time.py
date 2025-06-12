from datetime import date
from datetime import datetime

day = date.today()
print(day)
print(day.day)
print(day.month)
print(day.year)

new_data = date(year=2020, month=2, day=2)
print(new_data)

day_full = datetime.now()
print(day_full.second)