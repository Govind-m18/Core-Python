# 1. Write a program to check if the given number is positive or negative.

num = int(input("Enter a number : "))

if num % 2 == 0:
    print(f"{num} positive number")

else:
    print(f"{num} negative number")