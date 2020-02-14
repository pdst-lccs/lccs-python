
# Returns True if 'p' is a valid password
def isValidPassword(p):
    symbols = "_+-*/!?&^@"
    upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    
    # Cpncatenate the 4 strings into a single string of allowed characters
    allowed_chars = symbols + upper_case_letters + lower_case_letters + digits
    
    # Loop through each 'char' in 'p' to check validity
    for char in p:
        if char not in allowed_chars:
            return False
        
    # The loop has ended so the password must be valis - return True
    return True    


# Main program starts here
password = input("Enter a password: ")
if isValidPassword(password):
    print("%s is a valid password" %password)
else:
    print("%s is an invalid password" %password)
