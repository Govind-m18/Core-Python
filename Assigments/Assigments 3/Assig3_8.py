# WAP to prompt user to enter userID and password after verifying userID and Password display a 4 digit random number and ask user to enter the same . is user enter the same number then show him success messege otherwise failed .(something like captcha)


import random 

user_id = input("Enter user ID :")
password = input("Enter password :")

# varify user ID and Passwoed 

if user_id == "Govind_18" and password == "1433" :
    # GEnarate 2 digit random number 
    captcha = random.randint(1000,9999)

    print("your captcha is :",captcha)

    # ASK user to enter captcha

    user_captcha = int(input("ENter captcha :"))

    # varify captcha

    if user_captcha == captcha :
        print("Login Successfully ")
        if user_captcha == captcha :
            print("Welcome Govind_18")

    else :
        print("Captha failed..!")
        

else :
    print("Invalid id or password !")




