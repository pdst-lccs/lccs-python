# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Dictionary Programming Exercises 7.1
# Q2(b) solution


colours = dict({
    'white': "bán",
    'red': "dearg",
    'green' : "gorm",
    'blue' : "glas",
    'black' : "dubh",
})

print("BEFORE: ", colours)

colours['yellow'] = 'buí'
colours['pink'] = 'bán agus dearg'
colours['green'] = 'glas'
colours['blu'] = 'gorm'
colours.update(blue='gorm')
colours.update(green='gorm', blue='dubh')
del colours['white']

print("AFTER: ", colours)