"""
    Compute the price of a meal as follows by asking for the 
    price of child and adult meals, price of drink, the number of each, and 
    then the sales tax rate. Use these values to determine 
    the total price of the meal. Then, ask for the payment amount and
    compute the amount of change to give back to the customer
"""
# asking the users the following questions
price_child = float(input("What is the price of a child's meal? "))
price_adult = float(input("What is the price of an adult's meal? "))
price_drink = float(input("What is the price of drinks? "))
children = int(input("How many children are there? "))
adult = int(input("How many adults are there? "))

# Getting the subtotal of the meal
subtotal = (price_adult * adult) + (price_child * children) + ((children + adult) * price_drink)
print()
print(f"Subtotal: ${subtotal:.2f}")
print()

# Getting the sales tax rate and calculating it 
tax_rate = float(input("What is the sales tax rate? "))
sales_tax = (subtotal * tax_rate) / 100
print(f"Sales Tax: ${sales_tax:.2f}")

# Adding the sales_tax and subtotal together
total = sales_tax + subtotal
print(f"Total: ${total:.2f}")
print()

# Calculating the change of the customer 
amount = float(input("What is the payment amount? "))
change = amount - total
print(f"Change: ${change:.2f}")
