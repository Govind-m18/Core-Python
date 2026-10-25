# Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on folloeing condition

# a . chilren below 12 = 30 % discount
# b . senior citizen (above 59) = 50 % discount
# c . other need to pay full .

ticket_price = float (input("Enter ticket full ticket amount per person :"))

total_amount = 0

for i in range(1,6):
    age = int(input(F"Enter age of person {i}:"))

    if age < 12 :
        discount = ticket_price * 30 / 100
        amount = ticket_price - discount
        print("child : 30 % Discount")

    elif age > 59 :
        discount = ticket_price * 50 / 100
        amount = ticket_price - discount

    else:
        amount = ticket_price
        print("NO discount")

    print("Ticket amount :",amount)

    total_amount = total_amount + amount

    