# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 6.2 Summing Numbers
# A program to implement Gauss's formula to calculate the sum the first n integers


# Sum the first n integers (Gauss's Formula)
def gaussSumOfN(n):
    return n*(n+1)/2

result = gaussSumOfN(100)
print("Sum of 1 to 100 is %d" %result)