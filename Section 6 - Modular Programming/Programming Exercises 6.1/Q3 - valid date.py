# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Solution to programming exercises 6.1 Q3
# Purpose: A program to validate a date entered as dd, mm, yyyy

# returns True for leap years, False for non-leap years
def isLeap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Returns True if the date is valid; False otherwise
def isValidDate(d, m, y):

    # Ensure 21st century
    if (y < 2000):
        return False
    # Ensure the day is between 1 and 31
    if (d < 1 or d > 31):
        return False
    # Ensure the month is between 1 and 12
    if (m < 1 or m > 12):
        return False

    # April, June, September and November cannot have more than 30 days
    if (m == 4 or m == 6 or m == 9 or m == 11) and (d > 30):
        return False
    # All other months (except Feb) cannot have more than 31 days
    elif (m != 2) and (d > 31):
        return False
    # February. 
    else:
        # Leap years cannot have more than 29 days.
        if isLeap(y):
            if (d > 29):
                return False
        # non-leap years cannot have more than 28 days.
        else:
            if (d > 28):
                return False
            
    return True



dd = int(input("Enter day (dd): "))
mm = int(input("Enter month (mm): "))
yyyy = int(input("Enter year (yyyy): "))
if isValidDate(dd, mm, yyyy):
    print("Valid")
else:
    print("Invalid")