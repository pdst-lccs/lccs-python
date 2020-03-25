# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to count (and display) the average word length in a text
# Breakout 7.1 Frequency Counters
# Q2(h) - solution

from collections import Counter

# IMPORTANT: Copy the book into book.txt before running
bookFile = open("book.txt","r") # Open the file
textList = bookFile.read().split()
bookFile.close()


c = Counter(textList)
total = 0
count = 0
for word_pair in c.most_common():
    word = word_pair[0]
    total = total + len(word)
    count += 1

print("Average word length is %.2f letters" %(total/count))
