# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Breakout 6.4 Check digits

# Suggested Activities - EAN-8 barcodes

def extractDigit(i, n):
    """Extract the ith digit from n
       
       The rightmost digit is at position 0
       Digit positions are 76543210    
    """

    if i < 0:
        return -1
    
    return (n//pow(10, i))%10

def isValidEAN8(n):
    
    sum = 0
    for i in range(9):
        digit = extractDigit(i, n)
        
        # Q4 - if an extraction error occurs return False
        if digit == -1:
            print("Digit extraction error")
            return False
        
        if i%2 == 0:
            sum = sum + digit
        else:
            sum = sum + digit*3

        
    return sum%10 == 0

# Main processing starts here
print(isValidEAN8(53912343)) # true
print(isValidEAN8(96335074)) # false
print(isValidEAN8(12345670)) # true

