# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate string construction

# Initialise the output string
outStr = "The quick "

# Ask the user for a colour
colour = input("Please enter a colour: ")

# Concatenate the colour to the output
outStr = outStr + colour
outStr = outStr + " fox jumps over the lazy "

# Ask the user for an animal
animal = input("Please enter an animal: ")
outStr = outStr + animal
outStr = outStr + "!"

# Display the output
print( outStr )
