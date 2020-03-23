# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Solution: Programming Exercises 6.3 Q7
# Purpose: A program to determine and display the first 4 perfect numbers


# Determines if one number is a factor of the other
def isFactor(a1, a2):
    return a2 % a1 == 0

def isPerfect(n):

    total = 0
    for i in range(1, n):
        if isFactor(i, n):
            total = total + i

    return n == total

# Main program
count = 0
number = 1
while count < 4:
    if isPerfect(number):
        print(number)
        count = count + 1
    number = number + 1
    
# NOTE TO TESTERS:
# The first 5 perfect numbers are:
# 6, 28, 496, 8128, 33550336 and 8589869056
