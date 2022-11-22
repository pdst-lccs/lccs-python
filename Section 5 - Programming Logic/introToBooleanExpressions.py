# Event: LCCS Python Fundamental Skills Workshop
# Date: Nov 2022
# Author: Sinead Crotty, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to introduce Boolean expressions

# Literal expressions (literals)
print(1)
print(1.23)
print("Mary")

"""
# Arithmetic expressions
x = 2 + 3 # operators +, -, *, /, //, %, **
print(x)
y = x + 4.0
print(y)
print("Mary had a little " + "lamb")

# Boolean values
# Predict the answer - add comments
print(True)
print(False)
print(type(True))  #bool
print(type(False)) #bool
print(isinstance(True, int)) #True
print(int(True)) 
print(int(False))
print(True+5)

# Relational Operators - used to compare 2 (numeric) operands
# >, >=, <, <=, ==, !=
# Predict the answer - add comments
print(7 > 3)  #True
print(7 >= 3) #True
print(7 < 3)  
print(7 <= 3) 
print(7 == 3) 
print(7 != 3) 
# Precedence of arithmetic operators is higher than relational
print(7+1 > 3) #True

# Other operators - is, in
# Predict the answer - add comments
print(5 is 5) #True
print("rain" is "rain") #True
print("r" in "rain") #True
print("ai" in "rain") 
print("aeiou" in "rain") 

# Relational Operators - used to compare 2 strings
# Predict the answer - add comments
print("computer" == "computer") # True
print("computer" != "computer") # False
print("computer" == "COMPUTER") 
print("computer" != "COMPUTER") 

print("computer" > "abacus") # True
print("COMPUTER" > "abacus") # False
print(ord("a")) # --> 97
print(ord("c")) # --> 99
print(ord("C")) # --> 67
# Predict the answer - add comments
print("computer" < "COMPUTER") 
print("computer" > "COMPUTER") 

# Logical Operators - not, and, or (precedence)
# NOT
# not A is true if A is false
print(not(True)) #False
# Predict the answer - add comment
print(not(False))

# AND
# A and B is True if both A and B are True
print(False and False) #False
print(False and True) #False
print(True and False) #False
print(True and True) #True

print("1<2 and 2<1",1<2 and 2<1) #False
# Predict the answer - add comments
print("1<2 and 2<3",1<2 and 2<3) 

# OR
# A or B is True if either A or B are True
print(False or False) # False
print(False or True)  # True
print(True or False)  # True
print(True or True)   # True

print("1<2 or 2<1",1<2 or 2<1) #True

# Predict the answer - add comments
print("2<3 and 4<3:",2<3 and 4<3) #False
#Question - how could you make this True? Answers in the chat

# Truth table for AND
print("Truth table: AND")
print("A\tB\tOutput")
print("False\tFalse\t",False and False) # False
print("False\tTrue\t",False and True) # False
print("True\tFalse\t",True and False) # False
print("True\tTrue\t",True and True) # True

# Truth table for OR
print("Truth table: OR")
print("A\tB\tOutput")
print("False\tFalse\t",False or False) # False
print("False\tTrue\t",False or True) # True
print("True\tFalse\t",True or False) # True
print("True\tTrue\t",True or True) # True

# Boolean Variables sometimes called flags
# Uncomment the lines below and predict the output
isRaining = False
# if isRaining:
#     print("Bring your umbrella")
finished = True
# if finished:
#     print("Well done on completing the task!")
"""
