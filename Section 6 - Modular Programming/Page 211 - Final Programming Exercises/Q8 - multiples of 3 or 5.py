# Version 1. 997 iterations
# Version 2. There are 1000/3 + 1000/5 = 533 iterations - almost twice as fast as Version 1 (and no need to understand or)
def get_sum_of_multiples_v1():
    sum = 0
    for i in range(3, 1000):
        if i%3 == 0 or i%5 == 0:
            sum = sum+i
    return sum

def get_sum_of_multiples_v2():
    sum = 0

    for i in range(3, 1000, 3):
        sum = sum + i

    for i in range(5, 1000, 5):
        if i % 3 != 0:
            sum = sum + i

    return sum

# Version 3. Based on n(n+1)/2 formula
#S3 = 3+6+9+12+15+...+999 = 3*(1+2+3+...+333) = 3*333*334/2 = 166,833
#S5 = 5+10+15+...995 = 5*(1+2+3+...+199) = 5*199*200/2 = 99,500
#S15 = 15+30+45+...+990 = 15*(1+2+3+...+66) = 15*66*67/2 = 33,165
def get_sum_of_multiples_v3():
    sumOfThrees = 3*(333*334)/2
    sumOfFives = 5*(199*200)/2
    sumOfFifteens = 15*(66*67)/2

    sum = sumOfThrees + sumOfFives - sumOfFifteens
    return sum

# Main program
print(get_sum_of_multiples_v1())
print(get_sum_of_multiples_v2())
print(get_sum_of_multiples_v3())