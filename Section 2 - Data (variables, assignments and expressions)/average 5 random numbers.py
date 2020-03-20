# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Compute the average of 5 random numbers

# Program to multiply two randomly generated numbers
import random

low  = random.randint(1,100) 
high = random.randint(low,100)

# Generate the 5 random numbers
n1  = random.randint(low, high)
n2  = random.randint(low, high)
n3  = random.randint(low, high)
n4  = random.randint(low, high)
n5  = random.randint(low, high)

# Compute their average
average = (n1+n2+n3+n4+n5)/5

# Multiply the two numbers and display the result
print("The average of", n1, n2, n3, n4, n5, "is", average)
