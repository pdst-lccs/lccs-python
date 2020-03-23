# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Solution: Programming Exercises 6.3 Q5
# Purpose: A program to implement the Collatz sequence


# Read a valid number
def get_number(prompt):
    while True:
        strN = input(prompt)
        if strN.isdigit():
            break
        
    return int(strN)    

def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Main program
n = get_number("Enter a positive number: ")
while n <= 0:
    print("ERROR: The number must be positive")
    n = get_number("Enter a positive number: ")

while n != 1:
    if isEven(n):
        n = n/2
    else:
        n = 3*n+1
    print(int(n), end="->")
    
print("END!")
