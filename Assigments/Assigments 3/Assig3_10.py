# WAP to check if person is eligible to marry or not eligible to marry
# (male age >= 21) and (female age >= 18)

gender = input("Enter your gender (Male / Female) :").lower()

age = int(input("Enter your age :"))

if gender == "male" and age >=21 :
    print("you are eligibale to marry.")

elif gender == "female" and age >=18 :
    print("you are eligible to marry.")

elif gender == "male" and age <= 21 :
    print("you are not eligible to marry. ")

elif gender == "female" and age <= 18 :
    print("you are not eligible to marry.")

else:
    print("invalid gender plese try again after you decide your currect gender !")
