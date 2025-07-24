"""
Work along with your instructor to write a Python program that gets a customer’s subtotal as input and 
gets the current day of the week from your computer’s operating system. 
Your program must not ask the user to enter the day of the week. 
Instead, it must get the day of the week from your computer’s operating system.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, 
your program must subtract 10% from the subtotal. 
Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. 
Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.

Enhancements
1. Add code to your program that the computer will execute if today is Tuesday or Wednesday and 
the customer is not purchasing enough to receive the discount. 
This added code should compute and print the difference between $50 and the subtotal which is 
the additional amount the customer would need to purchase in order to receive the discount.
2. Near the beginning of your program replace the code that asks the user for the subtotal with a 
loop that repeatedly asks the user for a price and a quantity and computes the subtotal. 
This loop should repeat until the user enters "0" for the quantity.
"""

import datetime
import math

current_date = datetime.date.today()
day_of_the_week = current_date.strftime("%A")
keep_playing = "1"

while keep_playing != "0":
    amount = float(input("Please enter the amount of product: "))
    quantity = int(input("How many quantites did you want to pick: "))
    subtotal = amount * quantity
    print(f"The subtotal of your order is {subtotal}")
    if (day_of_the_week == "Tuesday" or day_of_the_week == "Wednesday"):
        if subtotal >= 50:
            discount = subtotal * 0.10
            tax_amount = (subtotal - discount) * 0.06
            total_amount = subtotal - discount + tax_amount 
        
            print(f"Discount amount: {discount:.2f}")
            print(f"Sales tax amount: {tax_amount:.2f}")
            print(f"Total: {total_amount:.2f}")

        else:
            tax_amount = subtotal * 0.06
            total_amount = subtotal + tax_amount
            print(f"Sales tax amount: {tax_amount:.2f}")
            print(f"Total: {total_amount:.2f}")
            balance = 50 - subtotal
            print(f"You need to additional purchase of {balance:.2f} to receive a discount")

    else:
        tax_amount = subtotal * 0.06
        total_amount = subtotal + tax_amount
        print(f"Sales tax amount: {tax_amount:.2f}")
        print(f"Total: {total_amount:.2f}")
    keep_playing= (input("Press 0 to end the program: "))
print("\nThank you")
