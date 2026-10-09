# Write a program to calculate area of an equilaterral triangle .

# Formula : area = (math.sqrt(3) / 4) * a * a


import math

a = float(input("Enter the side of an equilateral triangle: "))

area = (math.sqrt(3) / 4) * a * a

print("Area of an equilateral triangle =", area)
