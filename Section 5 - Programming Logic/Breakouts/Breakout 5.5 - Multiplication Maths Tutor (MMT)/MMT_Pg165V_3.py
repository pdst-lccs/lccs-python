'''multiplication tutor V3
the user should be provided with more detailed feedback 
about their answer i.e. correct, too high or too low'''

import random

n1 = random.randint(0, 12) # Generate the 1st number
n2 = random.randint(0, 12) # Generate the 2nd number
ans = n1*n2 # Calculate the product and store it in 'ans'

print("%d * %d" %(n1,n2))  # Display the expression
usrAns = int(input("Enter your answer: ")) # Read the response

# Evaluate the condition
if usrAns == ans:
   print("Correct!")
elif usrAns > ans:
   print("Too High!")
else:
    print("Too Low")

print("The correct answer was %d" %(n1*n2))
print("Goodbye")