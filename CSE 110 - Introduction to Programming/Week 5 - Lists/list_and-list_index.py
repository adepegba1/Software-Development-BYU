"""
Ask the user for a list of list of items in a shopping list, stop asking for items when the user types "quit."

Then complete the following:

Loop through the items in the regular way (for example, for thing in the_list) and 
display each one to make sure you have the initial list built correctly.

Add another loop to go through and print the items in the list, 
but this time, instead of using the for ... in syntax, use an index (for example, for ... in range) a
nd then access the item using the index and the square brackets. 
Print the index in front of the items like so: 0. Milk

Ask the user for an index and a new shopping list item. 
Replace the item at that index with the new item. 
Then, display the whole list again.
"""

shopping_list = []
item = ""
print("Please enter the items of the shopping list (type: quit to finish):" )

while item.lower() != "quit":
    item = input("Item: ")

    if item.lower() != "quit":
        shopping_list.append(item.title())

print("\nThe shopping list is:")

for i in shopping_list:
    print(i)

print("\nThe shopping list with indexes is:")

for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")

print()
index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

shopping_list.pop(index)
shopping_list.insert(index, new_item.title())

print("\nThe shopping list with indexes is:")

for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")
