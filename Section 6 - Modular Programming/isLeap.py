# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to determine whether a year is leap or not

def isLeap(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    else:
        return False

yr = int(input("Enter a year: "))
if isLeap(yr):
   print(yr, "is a leap year")
else:
   print(yr, "is NOT a leap year")
