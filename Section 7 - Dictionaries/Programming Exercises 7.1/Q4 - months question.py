# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Dictionary Programming Exercises 7.1
# Q4 - initial code


# A function to return the number of days in 'month_name'
def daysInMonth(month_name):
    if month_name == "February":
        return 28 # we ignore leap years!
    elif month_name in ("April", "June", "September", "November"):
        return 30
    elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
        return 31
    else:
        return

# Main Processing
print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")
numDays = daysInMonth(month_name)
if numDays == None:
    print("Invalid month entered")
else:
    print("No. of days: %d" %numDays)
    
