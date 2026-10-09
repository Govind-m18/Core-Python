# Write a Program to input two angles from user and find third angle of the triangle.

# Formula :

 # A + B + C = 180 
 # 60 + 60 + 60 = 180.  The sum of the three A, B, and C angles of a triangle is 180 .

# Third angle = 180 - (First angle + Second angle)

# Therefore, C = 180 - (A + B)

angle1 = float(input("Enter first angle of tringle: "))
angle2 = float(input("Enter second angle of tringle: "))

# Calculation for findind third angele (c = 180 - (A + b))

angle3 = 180 - (angle1 + angle2) 

print("Third angle of tringle is :", angle3)

