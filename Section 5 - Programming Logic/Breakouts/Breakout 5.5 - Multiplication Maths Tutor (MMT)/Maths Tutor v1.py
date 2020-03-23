# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: This code displays version 1 of Maths Multiplication Tutor (MMT v1)
# This is the base version of a program on which to complete Breakout Task 5.5

import random

n1 = random.randint(0, 12) # Generate the 1st number
n2 = random.randint(0, 12) # Generate the 2nd number
ans = n1*n2 # Calculate the product and store it in 'ans'

print("%d * %d" %(n1,n2))  # Display the expression
usrAns = int(input("Enter your answer: ")) # Read the response

# Evaluate the condition
if usrAns == ans:
   print("Correct!")

print("The correct answer was %d" %(n1*n2))
print("Goodbye")
