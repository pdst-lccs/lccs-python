# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Multiply 2 random numbers

# Program to multiply two randomly generated numbers
import random

num1 = random.randint(1,10) # generate a number between 1 and 10
num2 = random.randint(1,10) # generate a number between 1 and 10

# Multiply the two numbers and display the result
print(num1, "times", num2, "=", num1*num2)
