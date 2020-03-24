# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Dictionary Programming Exercises 7.1
# Q4 - solution

# A dictionary of the number of days in each month
days = {
   "January" : 31,
   "February" : 28, # ignore leaps!
   "March" : 31,
   "April" : 30,
   "May" : 31,
   "June" : 30,
   "July" : 31,
   "August" : 31,
   "September" : 30,
   "October" : 31,
   "November" : 30,
   "December" : 31,
}

# A function to return the number of days in month_name
def daysInMonth(month_name):
    return(days[month_name])


print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")
numDays = daysInMonth(month_name)
if numDays == None:
    print("Invalid month entered")
else:
    print("No. of days: %d" %numDays)
    

