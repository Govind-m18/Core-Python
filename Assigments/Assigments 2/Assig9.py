# WAP to swap two number withouy using third variable.

#FORMULA 

# A = A + B
# B = A - B 
# A = A - B

a = int(input("Enter first number:"))
b= int(input("Enter second number:"))

print("Before swapping:")
print("A = ",a)
print("B =",b)

a =a+b
b =a-b
a =a-b

print("After swapping :")
print("A = ", a)
print("b =",  b)
