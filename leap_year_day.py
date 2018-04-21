import calendar
import datetime
from datetime import date
import calendar


def get_leap_year(year):
    leap_year_counter = 0
    if calendar.isleap(year):
        my_date = datetime.datetime(year, 2, 29)
        print(calendar.day_name[my_date.weekday()])
    else:
        print('This is a not leap year')
        if year%2==0:
            year_before = year -2
            year_after = year+2
            year_before_date = datetime.datetime(year_before, 2, 29)
            year_before_day = calendar.day_name[year_before_date.weekday()]
            year_after_date = datetime.datetime(year_after, 2, 29)
            year_after_day = calendar.day_name[year_after_date.weekday()]
            print("Closest leap years days are"+" "+ str(year_before)+"-" + str(year_before_day)+","+str(year_after)+"-"+str(year_after_day))
        else:
            test_before = year -1
            if calendar.isleap(test_before):
                my_date = datetime.datetime(test_before, 2, 29)
                print("The closest leap year day is", calendar.day_name[my_date.weekday()])
            else:
                test_after = year+1
                my_date = datetime.datetime(test_after, 2, 29)
                print("The closest leap year day is",calendar.day_name[my_date.weekday()])


user_input = int(input("Please enter the year"))

get_leap_year(user_input)