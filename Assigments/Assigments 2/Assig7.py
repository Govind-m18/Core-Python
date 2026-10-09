## Find the sum of three - digit num

#FORMULA

# dupose the Three-digit number is N

# Hundreds digit = n//100
# Ten digit = (N // 10)%0
# Units digit = N % 10

# SUM = HUNDREDS + TENS + UNITS


num = int(input("Enter three - digit number:"))

hundreds = num // 100
tens = (num//10) % 10
units = num % 10

sum = hundreds + tens + units
print("sum of digits =",sum)