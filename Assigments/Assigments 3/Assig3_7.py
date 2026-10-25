# WAP to check if user has entered correct user ID and PASSWORD.

# LOGIC :

# We store a correct user ID and PASSWPRD then compare them with value entered by the user.

user_id = input("Enter usre id :")
password = input("Enter password :")

if user_id == "admin" and password == "12345" :
    print("correct user ID and PASSWORD")

else :
    print("Incorrect usr ID or PASSWORD")