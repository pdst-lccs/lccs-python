# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Name: Guessing Game v4
# Purpose: A program to demonstrate counter controlled repetition using while
# Description: The user is given 3 'chances'


import random

number = random.randint(1, 10)
print(number) # have a sneak peek!

# Initialise a loop counter
counter = 0

# Loop 3 times
while counter < 3:

    guess = int(input("Enter a number between 1 and 10: "))
    if guess == number:
        print("Correct")
        break # exit the loop immediately!
    elif guess < number:
        print("Too low")
    else:
        print("Too high")

    counter = counter + 1

print("Goodbye")

