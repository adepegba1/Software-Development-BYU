"""
For this project, the user will be given a menu and have the ability to choose items from the menu. 
The options in the menu include the following:

Add a new item
Display the contents of the shopping cart
Remove an item (only needed for the final project deliverable)
Compute the total (only needed for the final project deliverable)
Quit

When the user chooses one of these options, the program should perform the appropriate action. 
Then the program should show them the menu again, and allow them to choose another option. 
It should continue running until the user choose the option to quit.
The program also have quantities column. Asking the user how many quantities did they need
Then, the program calculate the amount for each item in the list
The program also inform the user if wrong option is selected
"""
print("Welcome to the shopping cart option\n")
print("""Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
""")
# creating empty list to how the item, prices, quantities
lists= []
prices = []
quantities = []
# Asking the user the action they want to perform
action = input("Please enter an action: ")

# while the action selected is not 5, the program will continue working.
while action != "5":
    # if action is 1, perform the block of code
    if action == "1":
        # Asking the user the following questions:
        item = input("\nWhat item would you like to add? ").title()

        price = float(input(f"What is the price of {item}? "))

        quantity =  int(input(f"How many quantities of {item} did you want? "))

        print(f"'{item}' has been added to the cart.")
        # based on the user input, the list is appended to each question respectively
        lists.append(item)
        prices.append(price)
        quantities.append(quantity)
    # if action is 2, perform this block of code
    elif action == "2":
        print("The contents of the shopping cart are:")
        print("   Item----------Prices-----Quantities------Amount")
        # Displaying the content of the shopping list with for loops
        for index in range(len(lists)):
            amount = prices[index] * quantities[index]
            print(f"{index+1}. {lists[index]}    -     ${prices[index]:,.2f}     -    {quantities[index]:,}     =    ${amount:,.2f}")
    # if action is 3, perform this block of code
    elif action == "3":
        # Printing out the content of the shopping cart for the user to select the one to remove     
        print("The contents of the shopping cart are:")
        print("   Item----------Prices-----Quantities------Amount")
        for index in range(len(lists)):
            amount = prices[index] * quantities[index]
            print(f"{index+1}. {lists[index]}    -     ${prices[index]:,.2f}     -    {quantities[index]:,}     =    ${amount:,.2f}")
        # Asking the user which item number did they want to remove
        remove = int(input("Which item number would you like to remove? "))
        # checking if the number is above the len of the list and return invalid to the user
        if remove > len(lists):
            print("\nSorry, that is not a valid item number")
        # if the number is within the len of the list, remove it in all the list
        else: 
            lists.pop(remove - 1)
            prices.pop(remove - 1)
            quantities.pop(remove - 1)

            print("\nItem Removed")
            # Displaying the new content after removing the item
            print("The new contents of the shopping cart are:")
            print("   Item----------Prices-----Quantities------Amount")
            for index in range(len(lists)):
                amount = prices[index] * quantities[index]
                print(f"{index+1}. {lists[index]}    -     ${prices[index]:,.2f}     -    {quantities[index]:,}     =    ${amount:,.2f}")
    # if the action is 4, perform this block of code
    elif action == "4":
        sum = 0
        for index in range(len(lists)):
            sum += (prices[index] * quantities[index])
        print(f"The total amount of the items in the shopping cart is ${sum:,.2f}")
    # if the action is not an action, display this block of code
    else:
        print("You type the wrong option. Try again")

    print("""\nPlease select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
""")
    
    action = (input("Please enter an action: "))
print("Thanks for shopping with us. Goodbye")