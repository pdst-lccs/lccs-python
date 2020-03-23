# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate the use of plotlty using factorials

import collections
import plotly
from plotly.graph_objs import Bar, Layout


# A recursive solution to factorial
def factorial(n):
    
    if n == 0:
        return 1
    
    return n * factorial(n-1)

# Main processing

nums = [] # An empty list of numbers
factList = [] # An empty list - for factorials

for i in range(5):
    nums.append(i)
    factList.append(factorial(i))
    

# Plot the results (x and y values must be in lists)
plotly.offline.plot({           
    "data": [Bar(x=nums, y=factList)],
    "layout": Layout(title="word count")
})
