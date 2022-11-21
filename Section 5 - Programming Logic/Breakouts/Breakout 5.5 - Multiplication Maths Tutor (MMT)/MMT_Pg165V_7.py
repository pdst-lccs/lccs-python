'''multiplication tutor V7
In this final version of the application, the functionality should remain exactly the same as 
version 6. However, this version should validate any data entered by the user i.e. it checks 
that the user’s answer is in fact a number before proceeding.
'''

import random

n1 = random.randint(0, 12) # Generate the 1st number
n2 = random.randint(0, 12) # Generate the 2nd number
ans = n1*n2 # Calculate the product and store it in 'ans'
print("%d * %d" %(n1,n2))  # Display the expression

print("You have as many chances you wish to get the correct answer to win.")

#initialiasing the loop guard variable
keepGoing=True

#loop guard. The loop will continue as long as keepGoing is True
while keepGoing:
       
   
    
    
    usrAns = input("Enter your answer: " ) # Read the response
     #To validate the users input to ensure the value is a number
    while not usrAns.isdigit():
        print("Please ensure you have entered a number")
        usrAns = input("Enter your answer: " ) # Read the response
    
    #convert ans to a integer
    usrAns=int(usrAns)
   
    
    # Evaluate the condition
    if usrAns == ans:
        
        print("Correct!")
        goAgain=input("Would you like like to go again Y or N?")
        #goAgain.upper() == "N" ensure if the user enter lowercase n,code will work
        
        if goAgain.upper() == "N":
            keepGoing = False #terminate the loop and game
        else:
            #Generate a new number
            n1 = random.randint(0, 12) # Generate the 1st number
            n2 = random.randint(0, 12) # Generate the 2nd number
            ans = n1*n2 # Calculate the product and store it in 'ans'
            print("%d * %d" %(n1,n2))  # Display the expression
        
    elif usrAns > ans:
         print("Too High!")
         
    else:
         print("Too Low")


print("Goodbye")