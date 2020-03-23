# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 6.2 Summing Numbers - Further Activities
# Q1 Sum of first N odd numbers

# Sum the first n integers (Gauss's Formula)
def sum_of_N(n):
    return n*(n+1)/2

def sum_of_even(n):
    return n*(n+1)

x = int(input("Enter a number: "))
ans = sum_of_N(2*x) - sum_of_even(x)
print ("The sum of the first %d odd numbers is %d" %(x, ans))


# Explanation.
# The sum of the 1st 10 odd numbers is 1+3+5+7+9+11+13+15+17+19 = 100
# This is the same as the sum of the first 20 numbers less the sum of the first 10 even numbers
# i.e. Sum of 1st 10 odds = (1+2+3+4+5+...+18+19+20) - (2+4+6+...+18+20)
# We are removing the first N even numbers
# As it turns out the sum of teh first n odd numbers is n^2
# Therefore the following statement would have done the job!
# print ("The sum of the first %d odd numbers is %d" %(x, x**2))