# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Dictionary Programming Exercises 7.1
# Q1(h) solution

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
print(car['model'])	
print(car['kms'])
print(car['colour'][0])	
print(car['diesel'])	
print(car['reg'][4:5])	
currentYear = 2018
print(car['kms']/(currentYear - car['year']))
