# Event: LCCS Python Fundamental Skills Workshop
# Date: May 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate string formatting

# Example 1
print("Example 1")
print("2 + %d = 4"   %2)
print("2 + %d = %d"  %(2, 4))
print("%d + %d = %d" %(2, 2, 4))
print("%d + %d = %d" %(2, 2, 2+2))

# Example 2
print("\nExample 2")
print("%s" %"String 1")
print("%s %s" %("String 1", "String 2"))
print("%s + %s = %d" %("2", "3", 2+3))
print("%d + %d" %(2, 3))
print("%d + %d = %d" %(2, 3, 2+3))
print("%f" %3.14)

# Example 3
print("\nExample 3")
# What do you think the following would display?
print("%s" %3)
print("%d" %3.14)
print("%f" %3)
#print("%f" %"Hi") # syntax error

# Example 4
print("\nExample 4")
msg = "Hi %s. How are you?"
name = "Hal"
print(msg%name)

# Example 5
print("\nExample 5")
# String formatting expressions are commonly used used with variables
import math
r = 5
print("Radius: %d, Area: %.2f" %(r, 2*math.pi*r))
