# WAP to print Fibonacci series upto n.

n = 10 # input for printing fibonacci series from 0 to 10 

a = 0 # First Fibonacci number
b = 1 # Second fibonacci number

count = 0 # Initialize counter 

while count <= n: # Repeat until n terms are printed

    print(a, end= " ")  # print the currect fibonacci serice

    c = a + b  # Calculate the next Fibonacci number
    a = b      # Update a with the value of b
    b = c      # Update b with the value of c

    count += 1 # Increase the counter by 1


    #OUTPUT IS = 0 1 1 2 3 5 8 13 21 34 55



