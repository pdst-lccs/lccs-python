'''multiplication tutor V6
This version should refine the previous version so that after entering the correct answer, the 
user is offered the opportunity to continue with a new expression. If the user enters “N” for 
no the application should exit. Otherwise the program should generate two new random 
number and the application should start again
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
      
    usrAns = int(input("Enter your answer: " )) # Read the response
    
    # Evaluate the condition
    if usrAns == ans:
        
        print("Correct!")
        goAgain=input("Would you like like to go again Y or N?")
                
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

   
print("The correct answer was %d" %(n1*n2))   
print("Goodbye")