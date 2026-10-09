# Write a program to enter P, T, R and calculate simple Interest.

# P = principal amount
# T = time period
# R = rate of interest

#formula for calculate simple interest

# simple_interesr = (p * t * r) / 100

P = float(input("Enter principal amount P: ")) #we can use  float() for give decimal value of principal amount.  ex : 6464.89
T = float(input("Enter time period T:"))
R = float(input("Enter rate of interest R:"))

simple_interest = (P * T * R) / 100 # calculatinf P, T, R for calculating simple interest.

print("simple interest:",simple_interest)

