'''multiplication tutor V2
the program should display a message informing the user that they were either 
correct or incorrect based on the value they enter.'''

import random

n1 = random.randint(0, 12) # Generate the 1st number
n2 = random.randint(0, 12) # Generate the 2nd number
ans = n1*n2 # Calculate the product and store it in 'ans'

print("%d * %d" %(n1,n2))  # Display the expression
usrAns = int(input("Enter your answer: ")) # Read the response

# Evaluate the condition
if usrAns == ans:
   print("Correct!")
else:
    print("Sorry but you are Incorrect!")

print("The correct answer was %d" %(n1*n2))
print("Goodbye")