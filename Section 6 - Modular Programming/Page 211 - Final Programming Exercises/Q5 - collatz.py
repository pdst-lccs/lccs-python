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
