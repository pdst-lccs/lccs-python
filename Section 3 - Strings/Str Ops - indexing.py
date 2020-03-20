# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate basic string indexing

# Initialise the string 
pangram = "The quick brown fox jumps over the lazy dog!"
#          01234567890123456789012345678901234567890123  

# INDEXING
print(pangram[0])
print(pangram[1])
print(pangram[2+4])
print(pangram[14])
print(pangram[8])
print(pangram[43])

# The index can be any valid Python expression
pos = 17
print(pangram[pos])
print(pangram[pos+1])

# A general pattern used to find the last character
print( pangram[len(pangram)-1] )
