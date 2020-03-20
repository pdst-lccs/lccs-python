# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to calculate the average height of 5 people

# A program to calculate the average height of 5 people
# The heights are stored in a file called 'heights.txt'

heightFile = open("heights.txt","r") # Open the file

totalHeight = 0 # Initialise a running total to zero
height = float(heightFile.readline())   # read the first value
totalHeight = totalHeight + height      # keep a running total

height = float(heightFile.readline())   # read the next value
totalHeight = totalHeight + height      # keep a running total

height = float(heightFile.readline())   # read the next value
totalHeight = totalHeight + height      # keep a running total

height = float(heightFile.readline())   # read the next value
totalHeight = totalHeight + height      # keep a running total

height = float(heightFile.readline())   # read the next value
totalHeight = totalHeight + height      # keep a running total

# Calculate the average
avgHeigth = totalHeight/5

# Display the result
print("The average height is "+str(round(avgHeigth,2))+"cm")
print("The average height is", round(avgHeigth*0.393701,2), "inches")

# Close the file
heightFile.close()
