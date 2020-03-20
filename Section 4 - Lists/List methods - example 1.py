# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate the use of list specific methods

# A short program to demonstrate the use of list specific methods
fruits = ['pear', 'apple', 'orange', 'banana', 'kiwi']
fruit = 'apple'
vegs = ['peas', 'carrots']


fruits.append(fruit)
print(fruits) # ['pear', 'apple', 'orange', 'banana', 'kiwi', 'apple']

fruits.extend(vegs)
print(fruits) # ['pear', 'apple', 'orange', 'banana', 'kiwi', 'apple', 'peas', 'carrots']

fruits.insert(2, fruit)
print(fruits) # ['pear', 'apple', 'apple', 'orange', 'banana', 'kiwi', 'apple', 'peas', 'carrots']

fruits.pop()
print(fruits) # ['pear', 'apple', 'apple', 'orange', 'banana', 'kiwi', 'apple', 'peas']

fruits.remove(fruit)
print(fruits) # ['pear', 'apple', 'orange', 'banana', 'kiwi', 'apple', 'peas']

fruits.reverse()
print(fruits) # ['peas', 'apple', 'kiwi', 'banana', 'orange', 'apple', 'pear']

fruits.sort()
print(fruits) # ['apple', 'apple', 'banana', 'kiwi', 'orange', 'pear', 'peas']

print(fruits.index(fruit)) # 0
print(fruits.count(fruit)) # 2
