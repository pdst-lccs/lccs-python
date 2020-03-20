# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to simulate a fruit (slot) machine

# Program to simulate a fruit machine!
import random

# initialise the list of fruits - 5 elements
fruits = ['Strawberry', 'Lemon', 'Orange', 'Raspberry', 'Cherry']

# generate three random numbers between 0 and 4 incl.
selection1 = random.randint(0, 4)
selection2 = random.randint(0, 4)
selection3 = random.randint(0, 4)

# show the results - display the fruits
print(fruits[selection1])
print(fruits[selection2])
print(fruits[selection3])

