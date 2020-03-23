# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Name: Guessing Game v4
# Purpose: A program to demonstrate counter controlled repetition using for
# Description: The user is given 3 'chances'

import random

number = random.randint(1, 10)
print(number) # For debugging purposes!

# Loop 3 times
for counter in range(3):

    guess = int(input("Enter a number between 1 and 10: "))
    if guess == number:
        print("Correct")
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")

print("Goodbye")

# Compare this version to the version that uses a while loop
# Notice how the variable counter is initialised differently?
