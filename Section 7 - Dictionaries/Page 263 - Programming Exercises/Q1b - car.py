# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Dictionary Programming Exercises

car = dict( {
    'reg': "131 CN 6439",
    'make': "Audi",
    'model' : "A6",
    'year' : 2013,
    'kms' : 52739,
    'colour': "Silver",
    'deisel': True,
})
print(car)


# The keys are reg, make, .... deisel
for k in car.keys():
    print(k)

# The values are 131 CN 6439, Audi, .... True
for v in car.values():
    print(v)