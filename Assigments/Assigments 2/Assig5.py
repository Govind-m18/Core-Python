# 5. WAP to calculate selling price of book based on cost price and discount.

cost_price = float(input("Enter cost price of bool:")) #2000
discount = float(input("Enter discount percentage:"))  #10

discount_amount=( cost_price* discount ) /100  #Discount 200
selling_price = cost_price - discount_amount   #selling price 1800

print("Discount Amount =", discount_amount)
print("Selling price =", selling_price)