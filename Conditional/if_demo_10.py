# Calculate Student Grade

marks = float(input("Enter percentage:"))

if marks < 0 or marks > 100:
    print("Invalid percentage")

elif marks >= 75:
    print("Distinction")

elif marks >= 60:
    print("First class")

elif marks >= 50:
    print("Second class")

elif marks >= 35:
    print("Pass class")

else:
    print("Fail")
