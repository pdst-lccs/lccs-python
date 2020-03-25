# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 7.1 Frequency Counters
# Q1(e) - solution 


# Count the number of characters in a sentence
sentence = input("Enter a sentence: ")
chars = {}
for char in sentence:
    chars[char] = chars.get(char, 0) + 1

print(chars)
