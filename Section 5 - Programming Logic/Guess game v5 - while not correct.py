# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Name: Guessing Game v5
# Purpose: A program to demonstrate sentinel controlled repetition using while
# Description: The user is given an unlimited number of chances

import random

number = random.randint(1, 10)
print(number) # have a sneak peek!

correct = False # initialise the loop guard variable

# Loop until the variable 'correct' becomes True (while correct == False)
while not correct: 

    guess = int(input("Enter a number between 1 and 10: "))
    if guess == number:
        print("Correct")
        correct = True # this will cause the loop to exit on the next iteration
    elif guess < number:
        print("Too low")
    else:
        print("Too high")


print("Goodbye")
