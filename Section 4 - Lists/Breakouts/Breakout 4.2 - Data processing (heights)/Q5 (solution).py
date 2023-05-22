# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2023
# Author: Computer Science, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to calculate the average height of 5 people, also min, max, range, median and mode

# A program to calculate the average height of 5 people
# The heights are stored in a file called 'heights.txt'
from statistics import mean, median, mode

heightFile = open("heights.txt","r") # Open the file

heights =[] # Initialise a list to store all the heights read in from the file
#totalHeight = 0 # Initialise a running total to zero
heights = heightFile.read()   # read the first value
heightsList = heights.split()
print(heightsList) #checking contents...

#Convert each element in the list from a string to a float
heightsList[0] = float(heightsList[0])
heightsList[1] = float(heightsList[1])
heightsList[2] = float(heightsList[2])
heightsList[3] = float(heightsList[3])
heightsList[4] = float(heightsList[4])

print(heightsList) #checking contents...

# Calculate the average
avgHeight = mean(heightsList)

# Display the result
print("The average height is "+str(round(avgHeight,2))+"cm")
print("The average height is", round(avgHeight*0.393701,2), "inches")

minHeight = min(heightsList)
maxHeight = max(heightsList)
heightRange = maxHeight-minHeight
median_height = median(heightsList)
#mode_height = mode(heightsList)

print("Min:",minHeight)
print("Min:",maxHeight)
print("Range:",heightRange)
print("Median:",median_height)
#print("Mode:",mode_height)

# Close the file
heightFile.close()
