'''multiplication tutor V5
the program should continue until the user gets the correct 
answer.'''

import random

n1 = random.randint(0, 12) # Generate the 1st number
n2 = random.randint(0, 12) # Generate the 2nd number
ans = n1*n2 # Calculate the product and store it in 'ans'
print("%d * %d" %(n1,n2))  # Display the expression
print("You have as many chances you wish to get the correct answer to win")

#initialiasing the loop guard variable
keepGoing=True

#loop guard. The loop will continue as long as keepGoing is True
while keepGoing: 
    
    
    usrAns = int(input("Enter your answer: " )) # Read the response
    
    # Evaluate the condition
    if usrAns == ans:
       print("Correct!")
       keepGoing=False #terminate the loop and game
    elif usrAns > ans:
       print("Too High!")
    else:
        print("Too Low")

    
print("The correct answer was %d" %(n1*n2))  
print("Goodbye")