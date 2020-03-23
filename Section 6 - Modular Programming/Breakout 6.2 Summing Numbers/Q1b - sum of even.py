# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 6.2 Summing Numbers
# Q1 b) Sum of first N even numbers

n = int(input("Enter a number: "))
print ("The sum of the first %d even numbers is %d" %(n, n*(n+1)))

# Explanation.
# The sum of the 1st 10 even numbers is 2+4+6+8+10+12+14+16+18+20 = 110
# This is the same as 2 times the sum of the first 10 numbers i.e. 2(1+2+3+4+5+6+7+8+9+10)
# But the sum of the first N numbers is (n/2)*(n+1) (i.e. Gauss's Formula)
# Therefore, the sum of the 1st N even numbers is n*(n+1)
