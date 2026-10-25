# WAP to calculate profit or loss

# Formula

# profit = selling price - cost price

# profit= SP - CP

# Loss = cost price - selling price

#Loss = CP - SP

cp = float(input("Enter cost price :"))
sp = float(input("Enter selling price :"))

if sp > cp :
    profit = sp - cp
    print("Profit",profit)

elif cp > sp :
    loss = cp - sp 
    print("Loss",loss)

else :
    print("No Profit , No Loss")