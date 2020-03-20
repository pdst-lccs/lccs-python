# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to simulate a fruit machine
# Description: To run this program the file fruits.txt must exist in the runtime folder
# This program reads the entire file in one command (read)
# The contents of the file are saved in a variable called fileContents
# The string is split into a list of tokens called fruits
# The choice command is used to select a random element from fruits

# Program to simulate a fruit machine!
import random

# Open the fruits file (already created)
fruitFile = open("fruits.txt","r")

# Read the entire file
fileContents = fruitFile.read()

# Close the file
fruitFile.close()

# Split the content into a list
fruits = fileContents.split()

# Spin! Display three fruits
print(random.choice(fruits))
print(random.choice(fruits))
print(random.choice(fruits))

# This line is just here for debugging purposes
# print(fruits) 


