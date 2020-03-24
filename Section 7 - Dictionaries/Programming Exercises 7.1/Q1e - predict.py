# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Dictionary Programming Exercises 7.1
# Q1(e) solution


car = dict( {
    'reg': "131 CN 6439",
    'make': "Audi",
    'model' : "A6",
    'year' : 2013,
    'kms' : 52739,
    'colour': "Silver",
    'diesel': True,
})

print(car['make'])
# print(car[model]) # NameError - model is not defined
# print(car['miles']) # KeyError - miles is not a key
print(car['colour'][0])
#print(car['diesel'][0]) # TypeError - cannot subscript a Boolean
print(car['reg'][4:5])
