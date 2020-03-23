# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to find the maximum of 3 values


# A function to find the largest of 3 numbers
def maxOf3(x, y, z):
    if (x > y) and (x > z):
        return x
    elif (y > x) and (y > z):
        return y
    elif (z > x) and (z > y):
        return z

# Test the function
print(maxOf3(1, 2, 3))
print(maxOf3(1, 3, 2))
print(maxOf3(3, 2, 1))
