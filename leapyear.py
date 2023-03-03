#Creating a function to determine whether a year is a leap year

def is_leap(year):
    #Return True for leap years, and False for non-leap years.

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = int(input('Enter a year: '))

print(is_leap(year))