# Find the Greatest of Two Numbers

a = int(input("Enter a number for A :"))
b = int(input("Enter a number for B :"))

if a > b:
    print(f"{a} is Greater than Number {b}")

elif b > a:
    print(f"{a} is Less than Number {b}")

else:
    print(f"{a} and {b} both are equel")