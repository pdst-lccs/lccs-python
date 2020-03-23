# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Solution to programming exercises 6.1 Q1
# Purpose: A program to list all the positive factors of ...
# ... any positive integer entered by the end user

# This function returns True if a1 is a factor of a2; Otherwise, False
def isFactorV1(a1, a2):
    if a2 % a1 == 0:
        return True
    else:
        return False

# This function returns True if a1 is a factor of a2; Otherwise, False
def isFactorV2(a1, a2):
    return a2 % a1 == 0

n = int(input("Enter a number: "))
for i in range(1, n+1):
    #if isFactorV1(i, n):
    if isFactorV2(i, n):        
        print(i)


