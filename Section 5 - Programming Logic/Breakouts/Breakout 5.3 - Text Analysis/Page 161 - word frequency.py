# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to count (and display) the most frequently occurring words in a text

import collections
import plotly
from plotly.graph_objs import Bar, Layout

# IMPORTANT: Copy the book into books.txt before running
bookFile = open("book.txt","r") # Open the file
textList = bookFile.read().split()
bookFile.close()

c = collections.Counter(textList)

words = []
wordCount = []

print ('Most common:')
for word, count in c.most_common(10):
    words.append(word) # append the word to the words list
    wordCount.append(count)
    print ('%s: %d' % (word, count))


# Plot the results (x and y values must be in lists)
plotly.offline.plot({           
    "data": [Bar(x=words, y=wordCount)],
    "layout": Layout(title="word count")
})
