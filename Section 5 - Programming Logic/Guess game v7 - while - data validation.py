
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Name: Guessing Game v7
# Purpose: A program to demonstrate data validation
# Description: This is the exact same as version 6 except the input is validated

# Guess Game v7 - while - go again? - data validation
import random

number = random.randint(1, 10)

# Initialise the loop guard variable
keepGoing  = True

# Loop as long as keepGoing is True
while keepGoing:

    guess = input("Enter a number between 1 and 10: ")
    # Validate. Make sure the value entered is numeric
    while not guess.isdigit():
       guess = input("Enter a number between 1 and 10: ")

    # Convert the string to an integer
    guess = int(guess)

    if guess == number:
        print("Correct")
        goAgain = input("Play again? (Y/N): ")
        if goAgain.upper() == "N":
            keepGoing = False
        else:
            # Get a new number
            number = random.randint(1, 10)

    elif guess < number:
        print("Too low")

    else:
        print("Too high")

print("Goodbye")
