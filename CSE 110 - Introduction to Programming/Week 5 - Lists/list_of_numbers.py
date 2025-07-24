"""
Ask the user for a series of numbers, and append each one to a list. Stop when they enter 0.
Once you have a list, have your program do the following:
Compute the sum, or total, of the numbers in the list.
Compute the average of the numbers in the list.
Find the maximum, or largest, number in the list.
Once the basic functionality is working, allow the user to enter both both positive and negative numbers, 
then find the smallest positive number (the positive number that is closest to zero).
"""
print("Enter a list of numbers, type 0 when finished.")
numbers = []
user_number = -1
sum = 0
max = 0
count = 0
min = 999999999999999
while user_number != 0:
    user_number = int(input("Enter a number: ")) 
    if user_number != 0:
        numbers.append(user_number)
        count += 1
        sum += user_number
        if user_number > max:
            max = user_number
        if user_number > 0 and user_number < min:
            min =user_number

        
print(f"The numbers are: {numbers}")
print(f"The sum is : {sum}")
print(f"The largest number is: {max}")
print(f"The average number is: {sum/count:.2f}")
print(f"The smallest positive number is: {min}")