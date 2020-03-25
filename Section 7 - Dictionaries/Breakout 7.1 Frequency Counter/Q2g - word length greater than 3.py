# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to count (and display) the most frequently occurring words in a text
# Breakout 7.1 Frequency Counters
# Q2(g) - solution

# IMPORTANT: Copy the book into book.txt before running
bookFile = open("book.txt","r") # Open the file
textList = bookFile.read().split()
bookFile.close()


# Ignore words of length 3 or less
from collections import Counter
c = Counter(textList)
index = 0
max_pair = c.most_common()[index]
word = max_pair[0] # The word is the first element of the pair (tuple)
while len(word) <= 3:
    index = index + 1
    max_pair = c.most_common()[index]
    word = max_pair[0]

   
print("%s occurs most often %d times" %(max_pair[0], max_pair[1]))