# Find the Greatest of Three Numbers

a = int(input("Enter number for A:"))
b = int(input("Enter number for B:"))
c = int(input("Enter number for C:"))

if a >= b and a >= c :
    print(f"{a} is greater than {b} and {c}")

elif b >= a and a >= c :
    print(f"{b} is greater than {a} and {c}")

else :
    print(f"{c} is greater than {a} and {b}")