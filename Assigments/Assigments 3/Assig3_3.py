# Write a program to input angles of a triangle and check whether triangle is valid or not.

a = float(input("Enter first angle of trangle A = "))
b = float(input("Enter second angle of trangle B = "))
c = float(input("Enter third angle of trangle c ="))

valid_trangle = a + b + c 

if valid_trangle == 180 :
    print("valid trangle")

else:
    print("not valid trangle")