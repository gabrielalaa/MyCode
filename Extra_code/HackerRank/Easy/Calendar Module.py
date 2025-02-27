import calendar

# print(calendar.TextCalendar(firstweekday=6).formatyear(2024))

# Method 1
month, day, year = map(int, input().split())
# Find the day
the_day_of_the_week = calendar.weekday(year, month, day)
# Print the name of the day in upper cases
print(calendar.day_name[the_day_of_the_week].upper())


# Method 2
import datetime
import calendar

m, d, y = map(int, input().split())
input_date = datetime.date(y, m, d)
print(calendar.day_name[input_date.weekday()].upper())