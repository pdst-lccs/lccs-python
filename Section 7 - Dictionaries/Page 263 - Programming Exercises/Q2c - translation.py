# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Dictionary Programming Exercises


colours = dict({
    'white': "bán",
    'red': "dearg",
    'green' : "gorm",
    'blue' : "glas",
    'black' : "dubh",
})

colour = input("Enter a colour (white, red, green, blue, black): ")
translation = colours[colour] # lookup using straightforward indexing

translation2 = colours.get(colour) # lookup using get
translation3 = colours.pop(colour) # lookup using pop

print(translation)
print(translation2)
print(translation3)
