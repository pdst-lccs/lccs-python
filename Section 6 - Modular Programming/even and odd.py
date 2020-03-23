# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate Boolean functions

# A function to determine evenness
def isEven(number):
    if (number % 2 == 0):
        return True
    else:
        return False

# display even numbers < 100
for i in range (100):
    if isEven(i):
        print(i)

'''
# A function to determine oddness
def isOdd(number):
    return not isEven(number)

for i in range (100):
    if isOdd(i):
        print(i)
'''
