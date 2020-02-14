# Section 2 - Programming Exercises Q4 (Zeller's Algorithm)

dd = int(input("Enter day of month: "))
mm = int(input("Enter the month (Mar=3, Apr=4, ... Jan=13, Feb=14): "))
yyyy = int(input("Enter the year (minus 1 for Jan or Feb): "))

y = yyyy%100   # last 2 digits of yyyy
c = yyyy//100  # first 2 digits of yyyy

w = (dd + (13*(mm+1)//5) + y + (y//4) + (c//4) - 2*c) % 7

print(w)


# Test this program using the data at the bottom of page 44
