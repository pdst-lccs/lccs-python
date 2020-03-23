# Event: LCCS Python Fundamental Skills Workshop
# Date: Dec 2018
# Author: Joe English, PDST
# eMail: computerscience@pdst.ie
# Purpose: A program to perform a compound interest calculation

# Calculates future value 
def future_value(principal, rate, time): 
    fv = principal * (pow((1 + rate / 100), time)) 
    return fv
  
# Driver Code
fv_A = future_value(10000, 5, 10)
fv_B = future_value(10000, 10, 5)
print("Scenario A: %.2f \nScenario B: %.2f" %(fv_A, fv_B))
