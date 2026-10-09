# WAP to reverse three-digit number.

# Supose the number is N = 123

# Last digit = N % 10
# Middle digit = (N//10)%10
# First digit = N //100            #Reverse = 3*100 + 2*10+1 =321

# Reverse = Last * 100 + middle * 10 + first



num = int(input("Enter a three-digit number:"))

a = num % 10
b = (num //10)%10
c = num // 100

reverse = a*100 + b*10 + c

print("Reverse number = ", reverse)