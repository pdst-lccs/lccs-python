# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: An averaging program

from statistics import mean

# Create an empty list to store the height values
heightList = []

# Open the file
heightFile = open("heights.txt","r")

# Read the 5 values into the list
height = float(heightFile.readline())
heightList.append(height)
height = float(heightFile.readline())
heightList.append(height)
height = float(heightFile.readline())
heightList.append(height)
height = float(heightFile.readline())
heightList.append(height)
height = float(heightFile.readline())
heightList.append(height)

# Close the file
heightFile.close()

# Calculate the arithmetic mean of the data in the list
meanHeight = mean(heightList)

# Display the result
print("The average height is "+str(round(meanHeight,2))+"cm")
print("The average height is", round(meanHeight*0.393701,2), "inches")

