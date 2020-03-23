# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Exercise on page 198 - encapsulate the code below into functions


# Part 1
year = int(input("Enter a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
   print(year, "is a leap year")
else:   
   print(year, "is NOT a leap year")

# Part 2
year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print(year, "is a leap year")
       else:
           print(year, "is NOT a leap year")
   else:
       print(year, "is a leap year")
else:
   print(year, "is NOT a leap year")


'''
# NOTE!
# Sometimes the standard library can contain what we're looking for!
from calendar import *

print(isleap(2000))
'''
