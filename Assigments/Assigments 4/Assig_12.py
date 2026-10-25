# 12. Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)


num = int(input("Enter a number :"))

temp = num 
digits = 0 

while temp > 0 :
    digits = digits + 1
    temp = temp // 10

temp = num
total = 0

while temp > 0 :
    digit = temp % 10
    total = total + digit ** digits
    temp = temp //  10


if num >= 0 and total == num :
    print(num,"is armstrong number")

else:
    print(num,"is not an armstrong number ")
