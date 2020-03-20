# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate basic string slicing

# Initialise the string 
pangram = "The quick brown fox jumps over the lazy dog!"
#          01234567890123456789012345678901234567890123  

# Extract from index 1 up to but NOT including index 5
print(pangram[1:5]) # "he q"

# Extract from index 17 up to but NOT including index 19
print(pangram[17:19]) # ox

print(pangram[:19])   # "The quick brown fox"
print(pangram[20:26]) # "jumps"
print(pangram[26:])   # "over the lazy dog!"
