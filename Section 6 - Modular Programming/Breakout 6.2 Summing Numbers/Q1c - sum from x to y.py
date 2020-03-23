# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 6.2 Summing Numbers
# Q1 c) Sum of all the positive integers from x to y

# Sum the first n integers (Gauss's Formula)
def sum_of_N(n):
    return n*(n+1)/2

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
if (x < y):
    z = sum_of_N(y) - sum_of_N(x-1)
    print("The sum of all the numbers from %d to %d is %d" %(x,y,z))
else:
    print("The second number must be greater than the first")

# Explanation.
# The sum of the numbers from x to y is the same as .....
# ... the sum of the numbers from 1 to y minus ...
# ... the sum of the numbers from 1 to x-1
# Example: The sum of the numbers from 8 to 13 = (1+2+3+...+11+12+13) - (1+2+3+...+6+7)
# So, sum(8..13) = sum(1..13) - sum(1..7)
# The reason we subtract sum(1..7) and not sum(1..8) is because we want to include 8 in the final sum
