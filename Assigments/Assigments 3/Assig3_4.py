# Write a program to input all sides of a triangle and check whether triangle is valid or
# not.


a = float(input("Enter first side of triangle :"))
b = float(input("Enter second side of triangle :"))
c = float(input("Enter third side of triangle :"))

# all_sides = a + b + c

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("Valid trangle")

else:
    print("Not valid tringle")