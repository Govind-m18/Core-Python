# WAP to check if given 3 digit number is a palindrome or not.

# a palindrom numbers is a numbers that remains the same when its digits are reversed

# ex :-
#      121 ----> is palindrome number
#      131 ----> is palindrome number
#      123 -----> it is not palindrome number

num = int(input("Enter a three digit number :"))

last = num % 10

last = num % 10

first = num // 100

if first == last :
    print(f"{num} is a palindrome number.")

else:
    print(f"{num} is not-palindrome.")

