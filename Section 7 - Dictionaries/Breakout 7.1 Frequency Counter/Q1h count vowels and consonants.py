# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 7.1 Frequency Counters
# Q1(h) - solution


# Count the number of vowels in a sentence
vowels = "aeiou"
sentence = input("Enter a sentence: ")
chars = {}
for char in sentence:
    if char in vowels:
        chars['vowels'] = chars.get('vowels', 0) + 1
    else:
        chars['consonants'] = chars.get('consonants', 0) + 1        
print(chars)


