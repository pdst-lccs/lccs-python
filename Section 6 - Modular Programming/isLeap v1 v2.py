# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate alternative implementations of isLeap

def isLeapV1(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 400 ==0:
        return True
    else:
        return False

# Subtle error here!
def isLeapV2(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 ==0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return False


# Main processing
yr = int(input("Enter a year: "))
if isLeapV1(yr):
   print(yr, "is a leap year")
else:
   print(yr, "is NOT a leap year")
