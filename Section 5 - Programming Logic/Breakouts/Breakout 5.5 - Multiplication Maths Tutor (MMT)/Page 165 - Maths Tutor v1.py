# Math multiplication tutor V1
import random

n1 = random.randint(0, 12) # Generate the 1st number
n2 = random.randint(0, 12) # Generate the 2nd number
ans = n1*n2 # Calculate the product and store it in 'ans'

print("%d * %d" %(n1,n2))  # Display the expression
usrAns = int(input("Enter your answer: ")) # Read the response

# Evaluate the condition
if usrAns == ans:
   print("Correct!")

print("The correct answer was %d" %(n1*n2))
print("Goodbye")
