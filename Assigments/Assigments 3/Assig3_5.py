# WAP a program to check whether the triangle is equilateral, isosceles or scalene triangle.

# Equilateral: All three sides are equal
# a==b==c

# isosceles: any two sidesd are aqual:
# a==b or b==c or a==c

# scalene: All three sides are diffirent
# a != b != c

a = float(input("Enter first side :"))
b = float(input("Enter second side :"))
c = float(input("Enter third side :"))

if a==b and b==c :
    print("Equilateral triangle ")

elif a == b or b == c or a == c :
    print("Isosceles triangle")

else:
    print("Scalene triangle")