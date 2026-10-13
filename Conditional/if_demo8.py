# Check Triangle Type Using Sides

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))


if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral triangle")
        

    elif a == b or b == c or a == c:
        print("Isosceles triangle")


    else:
        print("Scalene triangle")


else:
    print("Invalid triangle")
