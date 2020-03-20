# String Operation Activity

# Initialise four string variables
lowerLetters = "abcdefghijklmnopqrstuvwxyz"
upperLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
allLetters = lowerLetters+upperLetters
digits = "0123456789"

print(lowerLetters.upper())     # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(upperLetters.lower())     # "abcdefghijklmnopqrstuvwxyz"
print(upperLetters.find("h"))   # -1
print(lowerLetters.find("h"))   # 7
print(digits.count("123"))      # 1
print(lowerLetters.capitalize())# "Abcdefghijklmnopqrstuvwxyz"
print(digits.count("0"))        # 1
print(digits.lower())           # "0123456789"
print( min(allLetters) )        # "A"
print( max(allLetters) )        # "z"
print(allLetters.count("a"))    # 1
print(allLetters.count("aA"))   # 0
print(allLetters.count("ABC"))  # 1
print(digits.replace("0", "1")) # "1123456789"
print(allLetters.replace("ABC", "ABC")) # "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(allLetters.replace("xyz", "ABC")) # "abcdefghijklmnopqrstuvwABCABCDEFGHIJKLMNOPQRSTUVWXYZ"
