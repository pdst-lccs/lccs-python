# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate the use of parameters and arguments
# See Experiment on pages 184 and 185

def displayMessage(msg1, msg2):
    print(msg1)
    print(msg2)    
    # End of function

# The lines below are taken from the exercises on Pages 184 and 185
displayMessage("How are you today?", "Hello world")

displayMessage(1, 2)

# displayMessage(1, 2, 3)

displayMessage("Testing", 123)

# displayMessage("Testing", 1 2 3)

str1 = "Hello world"
str2 = "How are you today?"
displayMessage(str1, str2)
displayMessage(str2, str1)

str1 = "Dear "
str2 = "John"
displayMessage(str1+str2, "Hi!")

displayMessage(1+1, 2)
displayMessage("1+1=", 3)

pi = 3.14
r = 5
displayMessage("Area:", pi*r**2)
