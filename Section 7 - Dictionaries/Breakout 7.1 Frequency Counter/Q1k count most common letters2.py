# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 7.1 Frequency Counters
# Q1(k) - solution 

# Count the number of characters in a sentence
sentence = input("Enter a sentence: ")
chars = {}
for char in sentence:
    if char in chars:
        chars[char] = chars[char] + 1
    else:
        chars[char] = 1
print(chars)

# Another way of finding the most frequent letter
max_key = ""
max_value = 0
for k, v in chars.items():
    if v > max_value:
        max_value = v
        max_key = k

print("%s occurs most often %d times" %(max_key, max_value))
