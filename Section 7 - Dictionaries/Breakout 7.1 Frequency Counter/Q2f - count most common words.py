# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to count (and display) the most frequently occurring words in a text
# Breakout 7.1 Frequency Counters
# Q2(f) - solution

# IMPORTANT: Copy the book into book.txt before running
bookFile = open("book.txt","r") # Open the file
textList = bookFile.read().split()
bookFile.close()

# One way of finding the most frequent words
from collections import Counter
c = Counter(textList)

print ('The 10 most common words are:')
for word, count in c.most_common(10):
    print ('%s: %d' % (word, count))
