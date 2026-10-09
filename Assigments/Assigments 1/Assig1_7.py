# Program to Find the Roots of a Quadratic Equation

# The roots are calculated using the discriminant method.

# D = b**2 - 4*a*c
# If D > 0 --> Two different real roots.
# If D = 0 --> Two equal real roots.
# If D < 0 --> Two complex roots.

import cmath

a = float(input("Enter value of a:"))
b = float(input("Enter value of b:"))
c = float(input("Enter value of c:"))

# calculate the discriminant.

D = b**2 - 4*a*c

Root1 = ( -b + cmath.sqrt(D)) / (2*a) # using cmath.sqrt we can calculate the square root of a number including negative numbers
Root2 = (-b - cmath.sqrt(D)) / (2*a) # using this result in complex number.


print("Root 1 =",Root1)
print("Root 2 =",Root2)
