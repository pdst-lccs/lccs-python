# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate the use of functions to read an integer within a specified range


# Returns a number between 'lwr' and 'upr'
def readIntegerInRangeV1(lwr, upr):
    
    valid = False
    while not valid:
        strN = input("Enter a number: ")           
        if strN.isdigit():
            n = int(strN)
            if (n >= lwr) and (n <= upr):
                valid = True

    return n

# This function guarantees a number between 'lwr' and 'upr'
def readIntegerInRangeV2(lwr, upr):
    
    valid = False
    while not valid:
        strN = input("Enter a number: ")           
        if strN.isdigit():
            n = int(strN)
            if lwr <= n <= upr:
                valid = True

    return n


print(readIntegerInRangeV2(10,20))
