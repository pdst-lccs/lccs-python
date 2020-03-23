# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Program to keep a count of the number of times each face of a dice is rolled and plot the results
 
import random
import plotly
from plotly.graph_objs import *

faces=[1, 2, 3, 4, 5, 6] # A list of die face values
count=[0, 0, 0, 0, 0, 0] # A list for storing frequencies

for counter in range(1000):
    # loop body
    n = random.randint(1, 6)
    count[ n-1 ] = count[ n-1 ] + 1

# plot the results
plotly.offline.plot({
    "data": [Bar(x=faces, y=count)],
    "layout": Layout(title="Dice Results")
})

