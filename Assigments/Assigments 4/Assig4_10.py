# WAP to check if given number is Perfect Number.

n = int(input("Enter a number :"))

i = 1 
total = 0

while i < n:
    if n % i == 0:
        total = total + i

    i += 1

if n > 0 and total == n :
    print(n,"is a perfect number")

else :
    print(n,"is not perfect number")