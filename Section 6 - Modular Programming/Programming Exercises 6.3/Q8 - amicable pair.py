# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Solution: Programming Exercises 6.3 Q8
# Purpose: A program to determine if two integers are amicable pairs

# Determines if one number is a factor of the other
def isFactor(a1, a2):
    return a2 % a1 == 0

# Returns a list containing all the factors of n
def sumFactors(n):

    total = 0
    for i in range(1, n):
        if isFactor(i, n):
            total = total + i

    return total

# 
def isAmicable(n1, n2):
    return ((sumFactors(n1) == n2) and
            (sumFactors(n2) == n1))


# Read a valid number
def get_number():
    while True:
        strN = input("Enter a number: ")
        if strN.isdigit():
            break
        
    return int(strN)

# Main program
x = get_number()
y = get_number()
if isAmicable(x, y):
    print("%d and %d are an amicable pair" %(x,y))
else:
    print("%d and %d are not an amicable pair" %(x,y))

# NOTE TO TESTERS:
# The first ten amicable pairs are:
# (220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368),
# (10744, 10856), (12285, 14595), (17296, 18416), (63020, 76084), and (66928, 66992)

# An interesting extension to this exercise would be to determine and display the first ten amicable pairs 