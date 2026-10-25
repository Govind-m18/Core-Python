# input 5 sunject mark from user and display gread (eg. First class , Second class .)


sub1 = float(input("Enter marks of subject 1 :"))
sub2 = float(input("Enter marks of subject 2 :"))
sub3 = float(input("Enter marks of subject 3 :"))
sub4 = float(input("Enter marks of subject 4 :"))
sub5 = float(input("Enter marks of subject 5 :"))

total = sub1 + sub2 + sub3 + sub4 + sub5

percentage = total / 5

print("Total marks :",total , " / 500")
print("percentage ",percentage,"%")

if percentage >= 75 :
    print("Grade : Distinction")

elif percentage >= 60 :
    print("Grade : First class")

elif percentage >= 50 :
    print("Grade : Second class")

elif percentage >= 34 :
    print("Grade : pass")

else :
    print("Traval bro exploar the word life is beutifull")