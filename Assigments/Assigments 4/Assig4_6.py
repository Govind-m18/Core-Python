# WAP to check if a given number is prime number or not.

n = int(input("Enter a number :"))

if n <= 1 :
    print(n,"is not a prime number")

else:
    i = 2

    while i < n:
       if n % i == 0:
        print(n,"is not a prime number")

        break

       i += 1
    else:
       print(n,"is a prime number")


