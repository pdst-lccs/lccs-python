'''multiplication tutor V4
the program should use a while loop to give the 
user at most three chances to get the correct answer'''

import random
n1 = random.randint(0, 12) # Generate the 1st number
n2 = random.randint(0, 12) # Generate the 2nd number
ans = n1*n2 # Calculate the product and store it in 'ans'
print("%d * %d" %(n1,n2))  # Display the expression   
print("You have 3 chances to get the corrent answer to win")
counter=0
while counter<3: #loop guard
       
    usrAns = int(input("This is turn number %d. Enter your answer: " %(counter+1))) # Read the response
    
    # Evaluate the condition
    if usrAns == ans:
       print("Correct!")
       break #leave the loop immediately
    elif usrAns > ans:
       print("Too High!")
    else:
        print("Too Low")
            
    counter=counter+1#increments the counter
print("The correct answer was %d" %(n1*n2))   
print("Goodbye")
