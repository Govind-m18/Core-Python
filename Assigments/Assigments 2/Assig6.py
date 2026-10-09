# WAP to calculate total salary of employee based on basic 
# da=10% of basic, ta = 12% of basic hra = 15% of basic.


# DA = 10% * Basic
# TA = 12% * Basic
# HRA = 15% * Basic

# Total salary + Basic + DA + TA + HRA


basic = float(input("Enter basic salary:"))

da  = (10/100)*basic
ta  = (12/100)*basic
hra = (15/100)*basic

total_salary = basic + da + ta + hra

print("DA  = ",da)
print("TA  = ",ta)
print("HRA = ",hra)
print("Total salary = ", total_salary)