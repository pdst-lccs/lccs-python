# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate recursion

def fib(n):
   """Recursive function to
   return the nth Fibonacci number """
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))

# Test loop
# Display the first 10 numbers in the Fibonacci sequence
for i in range(10):
    print(fib(i), end=" ")
