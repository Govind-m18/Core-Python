# Write a program to convert days into years, weeks and days.

# Assuming

# 1 year = 365 days 
# 1 Weak = 7 days

days = int(input("Enter number of days :")) #input numbers of day :

# calculating years 

Years = days // 365 #this formula are used for converting days into years.

# find remaining days

remaining_days = days % 365 #modulus are used for remainig.

# calculating Weeks 

Week = remaining_days // 7

# find remining days .

remining_days = remaining_days % 7

#Display years, weeks , days

print("Years =",Years)
print("Week =",Week)
print("Days =",remining_days)





