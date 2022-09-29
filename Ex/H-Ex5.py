""" An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

Task

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

Input Format

Read Year, the year to test.

Constraints
1990<=year<=10**5

Output Format

The function must return a Boolean value (True/False). Output is handled by the provided code stub. """


def is_leap(year):
    leap = False
    lp=range(1900,(10**5)+1)
    mod4=year%4
    mod100=year%100
    mod400=year%400
    if year in lp and mod4==0 and mod100==0 and mod400==0:
        leap=True
        return leap
    elif  year in lp and mod4==0 and mod100!=0:
        leap=True
        return leap
    elif year not in lp:
        print("year out of range") 
    else:
        return leap

year = int(input())
print(is_leap(year))