# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to count (and display) the most frequently occurring words in a text using dictionaries

import collections
import plotly
from plotly.graph_objs import Bar, Layout

# IMPORTANT: Copy the book into book.txt before running
bookFile = open("book.txt","r") # Open the file
textList = bookFile.read().split()
bookFile.close()


c = collections.Counter(textList)
d = dict(c.most_common(10))

# Plot the results (x and y values must be in lists)
plotly.offline.plot({           
    "data": [Bar(x=list(d.keys()), y=list(d.values()))],
    "layout": Layout(title="word count")
})



'''
import operator
words = {}
for word in textList:
    words[word] = words.get(word, 0) + 1
t = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
t1 = t[:10]
print(t1)
'''


'''
print ('Most common:')
print(c.most_common(10))
for word, count in c.most_common(10):
    d[word] = count
    #print ('%s: %d' % (word, count))

print(d)
'''


'''
# Plot the results (x and y values must be in lists)
plotly.offline.plot({           
    "data": [Bar(x=words, y=wordCount)],
    "layout": Layout(title="word count")
})

'''
