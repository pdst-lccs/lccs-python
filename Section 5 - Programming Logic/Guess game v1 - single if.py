# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Name: Guessing Game v1
# Purpose: A program to demonstrate the single if statement

import random

number = random.randint(1, 10)
print(number)

guess = int(input("Enter a number between 1 and 10: "))

# Evaluate the condition
if guess == number:
    print("Your guess was correct")
    print("Well done!")

print("Goodbye")
