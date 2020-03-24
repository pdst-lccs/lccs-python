# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Dictionary Programming Exercises 7.1
# Q2(c) solution


colours = dict({
    'white': "bán",
    'red': "dearg",
    'green' : "gorm",
    'blue' : "glas",
    'black' : "dubh",
})

colour = input("Enter a colour (white, red, green, blue, black): ")

# A - lookup using the value of colour as the index
translation = colours[colour]

# B - lookup using get
translation2 = colours.get(colour) 

# C - lookup using pop
translation3 = colours.pop(colour) # lookup using pop

print(translation)
print(translation2)
print(translation3)
