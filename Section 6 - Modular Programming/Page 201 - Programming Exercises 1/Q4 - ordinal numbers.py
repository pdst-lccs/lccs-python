# Returns the correct ordinal suffix for num (attached to num)
def ordinal( num ):

    suffix = ['th', 'st', 'nd',
              'rd', 'th', 'th',
              'th', 'th', 'th', 'th']

    if num % 100 in (11,12,13):
        s = 'th'
    else:
        s = suffix[num % 10]

    return str(num) + s

# Read a valid number
def get_number():
    while True:
        strN = input("Enter a number: ")
        if strN.isdigit():
            break
        
    return int(strN)    


# Main program
number = get_number()
print(ordinal(number))