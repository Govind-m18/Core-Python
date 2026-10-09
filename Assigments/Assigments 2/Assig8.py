# WAP to swap two numbers using third variable.

#FORMULA

# To swap two numbers using a third variable:

# temp = A
# A = B
# B = temp

a = int (input("Enter first number:")) #a = 1
b = int(input("Enter second number:")) #b = 2

print("Befor swapping:")
print("A =",a) #A = 1
print("B =",b) #B = 2


temp = a
a = b
b = temp

print("After swaping:")
print("A=",a) #A = 2
print("B=",b) #B = 1




