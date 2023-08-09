#user input year and month display monthly calender

import calendar
year = int(input("Please Enter the year in yyyy:"))
month = int(input("Please Enter the Month mm: "))

print(calendar.month(year,month))