# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 6.2 Summing Numbers - Further Activities
# Q4 Approximate Euler's constant, e


# A function to return an estimate for Euler's constant
def approximate_e(precision):
    approx = 1
    factorial = 1

    for count in range(1, precision+2):
        factorial = factorial * count
        approx = approx + 1/factorial
            
    return approx

x = int(input("Enter the number of terms to use: "))
ans = approximate_e(x)
print ("Estimate for e using %d terms is %.6f" %(x, ans))
