
# Determines if one number is a factor of the other
def isFactorV1(a1, a2):
    if a2 % a1 == 0:
        return True
    else:
        return False

# Determines if one number is a factor of the other
def isFactorV2(a1, a2):
    return a2 % a1 == 0

n = int(input("Enter a number: "))
for i in range(1, n+1):
    #if isFactorV1(i, n):
    if isFactorV2(i, n):        
        print(i)


