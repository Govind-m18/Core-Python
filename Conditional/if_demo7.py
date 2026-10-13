# Check Triangle Validity Using Angles


a = float(input("Enter a first angle :"))
b = float(input("Enter a second angle :"))
c = float(input("Enter a third angle :"))

if a > 0 and b > 0 and c > 0 and a + b + c == 180:
    print("Valid triangle")

else:
    print("Invalid triangle")
