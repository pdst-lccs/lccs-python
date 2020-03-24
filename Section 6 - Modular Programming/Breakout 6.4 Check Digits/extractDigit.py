# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Breakout 6.4 Check digits
# Solution to Exercise 1 - extract the ith digit from n

# A function to extract digit i from number n
def extractDigit(i, n):
    i = len(n) - i
    if i < 0:
        return -1
    
    n = int(n)
    return (n//pow(10, i))%10

x = input("Enter a number: ")
pos = int(input("Enter position of digit to extract: "))
print(extractDigit(pos, x))



# The code snippets below will serve to provide a useful background

'''
n = int(input("Enter a 2 digit number: "))
d2 = n%10       # %10 extracts the final digit
d1 = n//10      # //10 to remove the final digit
print(d1, d2)
'''

'''
n = int(input("Enter a 3 digit number: "))
d1 = n%10         # %10 to extract the final digit
d2 = (n//10)%10   # //10 to remove the final digit
d3 = (n//100)  # //100 to remove the final two digits
print(d1, d2, d3)
'''

'''
n = int(input("Enter a 4 digit number: "))
d1 = n%10         # %10 extracts the final digit
d2 = (n//10)%10   # //10 chops off the last digit
d3 = (n//100)%10  # //100 chops off the last two digits
d4 = (n//1000)%10 # //1000 chops off the last three digits
print(d1, d2, d3, d4)
'''

'''
n = input("Enter a number: ")
numDigits = len(n)
n = int(n)

d = n%10  # %10 to extract the final digit
print(d, end=' ')
for count in range(1, numDigits):
    d = (n//pow(10, count))%10
    print(d, end=' ')    
print("")
'''


'''
def extractDigit2(i, n):

    if i <= 0 or i>= len(n):
        return -1
    
    return (n[i-1])


n = input("Enter a number: ")
print(extractDigit2(0, n))
'''
