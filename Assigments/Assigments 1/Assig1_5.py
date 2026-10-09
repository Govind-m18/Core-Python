# Write a program to enter P, T, R and calculate Compound Interest.

p = float(input("Enter principal amount P: ")) 
t = float(input("Enter time period T:"))
r = float(input("Enter rate of interest R:"))

compound_interest = p * (1 + r / 100) ** t - p 

print("Compound interest:",compound_interest)

