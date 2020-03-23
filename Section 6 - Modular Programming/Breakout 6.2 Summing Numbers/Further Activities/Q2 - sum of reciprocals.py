# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 6.2 Summing Numbers - Further Activities
# Q2 Sum of first N reciprocal

def sum_of_reciprocals(n):
    total = 0
    for i in range(1, n+1):
        total = total + 1/i
    return total    

x = int(input("Enter a number: "))
ans = sum_of_reciprocals(x)
print ("The sum of the first %d reciprocals is %f" %(x, ans))
