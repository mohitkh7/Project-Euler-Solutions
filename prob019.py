"""
Counting Sundays
Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

days_in_month_arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# month_name_arr = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
# day_name_arr = ["mon", "tues", "wed", "thur", "fri", "sat", "sun"]
sunday_count = 0
days = 1
for month_count in range((12 * 100)):
    # turning month count in range of 0 - 11
    month_index = month_count % 12
    year = 1901 + (month_count // 12)

    # counting if day is sunday
    if (days % 7) == 6:
        sunday_count += 1

    days += days_in_month_arr[month_index]
    # Adding aditional day for leap year
    if year % 4 == 0 and month_index == 1:
        days += 1

print(sunday_count)
