# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: Solution to re-ordering exercise (programming exercise 5.1)

import random

n1 = random.randint(0, 12) 
n2 = random.randint(0, 12)

print("%d * %d" %(n1,n2))  # Display the expression
ans = int(input("Enter your answer: ")) # Read the response

if ans == n1*n2:
   print("Correct!")
else:
   print("Incorrect!")
   
print("The correct answer was %d" %(n1*n2))
print("Goodbye")

# The following three lines were surplus to requirements
#ans = n1*n2
#if ans = n1*n2:
#n1*n2 = ans
