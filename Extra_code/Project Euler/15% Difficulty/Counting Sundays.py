# 1 Jan 1900 was a Monday -> 7 was a Sunday

# 30 days has Sept, April, June, Nov (4 months)
# 7 months have 31 days

# Feb has 28; but on leap years 29
# leap year on any year % 4; but not on a century unless it is divisible by 400

months = {'Jan': 31, 'Feb': 0, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def go_in_time():
    day_of_week = 0  # Monday
    number_of_sundays = 0

    # Start with the correct year
    for year in range(1900, 2001):
        # Set the number of days for Feb
        if leap_year(year):
            months['Feb'] = 29
        else:
            months['Feb'] = 28

        for month in months:
            # Check if we are between 1901-2000 and the first day of the month is sunday
            if year >= 1901 and day_of_week == 6:
                number_of_sundays += 1

            # Calculate the first day of the next month
            day_of_week = (day_of_week + months[month]) % 7

    return number_of_sundays

print(go_in_time())