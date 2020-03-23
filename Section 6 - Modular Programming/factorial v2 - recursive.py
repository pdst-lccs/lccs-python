# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate a recursive computations of factorial


# A recursive solution to factorial
def factorial(n):
    
    if n == 0:
        return 1
    
    return n * factorial(n-1)


# Test the function 
x = 5
print("%d! = %d" %(x, factorial(5)))

