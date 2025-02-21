""" 
Adding drinks, and tip to the total meal price
The program also asks for the price and quantity of drinks and calculates the tip based on a percentage provided by user
"""

# Asking the price of meals and quantity of persons
p_child = float(input(f"What's the price of a child's meal? "))
p_adult = float(input(f"What is the price of an adult's meal? "))
h_child = int(input(f"How many children are there? "))
h_adult = int(input(f"How many adults are there? "))

print ()

# Asking the price and quantity of drinks:
drink_price = float(input("What is the price of a drink? "))
quant_drinks = float(input("How many drinks do you want? "))

print()

# Calculating the subtotal 
subtotal = (p_child * h_child) + (p_adult * h_adult) + (drink_price * quant_drinks)
print(f"Subtotal: ${subtotal:.2f}")

print()

# Asking the sales tax rate and calculating it
tax_rate = float(input(f"What is the sales tax rate? "))
sales_tax = (tax_rate / 100) * subtotal 
print(f"Sales Tax: ${sales_tax:.2f}")

print()

# Asking the percentage of the tip and calculatin it
perc_tip = float(input(f"What percentage would you like to tip? "))
tip = (perc_tip / 100) * subtotal

print()

# Total
total = subtotal + sales_tax + tip 
print(f"Total: ${total:.2f}")

print()

# Payment Amount and Change
payment_amount = float(input(f"What is the payment amount? "))
change = (print(f"Change: ${payment_amount - total:.2f}"))



