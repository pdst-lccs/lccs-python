# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Name: Guessing Game v3
# Purpose: A program to demonstrate the multiple if statement

import random

number = random.randint(1, 10)
# The next line can be commented out later ...
print(number) # have a sneak peek at the number to guess!

guess = int(input("Enter a number between 1 and 10: "))

# Evaluate the condition
if guess == number:
    print("Correct")
    print("Well done!")
elif guess < number:
    print("Hard luck!")    
    print("Too low")
else:
    print("Hard luck!")    
    print("Too high")


print("Goodbye")
