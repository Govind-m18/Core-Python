# Find the area and circumference of circle.

# Formula :
 
# Area of a Circle: 
                    #    Area = π × r × r # R = radius of the circle

# Circumference of a Circle:
                         #   Circumference = 2 × π × r
# π(pi)=3.14159


import math #The math module provides mathematical functions and constants

radius = float(input("Enter the redius of circle :"))

area = math.pi * radius ** 2  #math.pi gives the value of π (approximately 3.14159). If r = 5, then Area = 3.14159 × 5 × 5.
circumference = 2 * math.pi* radius #If r = 5, then Circumference = 2 × 3.14159 × 5. 


print("Area of circle =",area)
print("Circumference =", circumference)