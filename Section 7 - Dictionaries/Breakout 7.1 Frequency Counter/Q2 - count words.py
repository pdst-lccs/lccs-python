# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Breakout 7.1 Frequency Counters
# Q2 - initial question

# Count the number of words in a sentence (v1)
sentence = input("Enter a sentence: ")
sent_list = sentence.split()
words = {}
for word in sent_list:
    if word in words:
        words[word] = words[word] + 1
    else:
        words[word] = 1
    
print(words)

