# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 6.2 Summing Numbers - Further Activities
# Q3 Approximate pi

def approximate_pi(precision):
    approx = 4
    sign = 1
    # Start the loop at 3 and use a step of 2
    for divisor in range(3, precision+5, 2):
        sign = sign * -1 # flip the sign on each iteration
        # print(sign, divisor) # handy debug information
        approx = approx + sign*(4/divisor)
            
    return approx

x = int(input("Enter the number of terms to use: "))
ans = approximate_pi(x)
print ("Estimate for pi using %d terms is %.6f" %(x, ans))

# NOTE:
# 'precision' is the number of terms to use in the calculation
# The reason we added 5 to 'precision' in the for statement was because:
# a) the first term is 4 and
# b) we start the loop iteration on 3 (as 3 is the first divisor in the formula) and
# c) we want to include the final term (range does not include the final value)