# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Name: Guessing Game v6
# Purpose: A program to demonstrate sentinel controlled repetition using while
# The program also demonstrates the use of nested if statements.
# Pay careful attention to the indentation
# Description: After a correct guess the player is given the option of playing another game


# Guess Game v6 - while not correct - ask, go again?
import random

number = random.randint(1, 10)
print(number) # have a sneak peek!

# Initialise the loop guard variable
keepGoing  = True

# Loop as long as keepGoing is True (while keepGoing == True)
while keepGoing:

    guess = int(input("Enter a number between 1 and 10: "))

    if guess == number:
        print("Correct")
        goAgain = input("Play again? (Y/N): ")
        if goAgain == "N":
            keepGoing = False
        else:
            # Generate a new number (for the player to guess)
            number = random.randint(1, 10)
            print(number) # why not?

    elif guess < number:
        print("Too low")

    else:
        print("Too high")


print("Goodbye")
