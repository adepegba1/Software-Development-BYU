"""
You are required to complete a Python script that performs basic arithmetic operations with two predefined numbers. The script should do the following:
1.	Assign specific values to two variables, number1 and number2.
2.	Perform addition, subtraction, and multiplication on these numbers.
3.	Print the results of these operations in a human-readable format
"""
x = float(input("Please enter the first number: "))
y = float(input("Pease enter the second number: "))
print(f"The addition of {x} and {y} is {x + y}")
print(f"The substraction of {x} and {y} is {x - y}")
print(f"The multiplication of {x} and {y} is {x * y}")
print(f"The division of {x} and {y} is {x / y}")

"""
to complete a Python script that calculates the simple interest earned on an investment over a period of time. The formula for simple interest is (I = P * R * T), where:
( I ) is the interest earned,
( P ) is the principal amount (initial investment),
( R ) is the annual interest rate (as a decimal),
( T ) is the time the money is invested for in years.•	Define three variables in this file:
o	principal with a value of 1000 (representing $1000),
o	rate with a value of 0.05 (representing 5% annual interest rate),
o	time with a value of 3 (representing 3 years).
•	Calculate the simple interest using the formula provided and store the result in a variable named interest.
•	Print the calculated interest in a format: The simple interest is: [interest].
"""
principal = float(input("What is the principal amount?: "))
rate = float(input("What is the percentage rate of the amount (%): "))
time = float(input("How many years did you want to invest the money?: "))
interest = (principal * rate * time) / 100
print(f"The simple interest for the money is {interest:.2f}")

"""
Use basic Python arithmetic operations and variable assignments to calculate the area of a rectangle using its length and width.  •	Define two variables in this file:
o	length with a value representing the length of the rectangle.
o	width with a value representing the width of the rectangle.
•	For simplicity, let’s use length = 10 and width = 5.
•	Calculate the area of the rectangle using the formula (Area = length × width) and store the result in a variable named area.
•	Print the calculated area in a format: The area of the rectangle is: [area].
"""
length = int(input("What is the length of the rectangle: "))
width = int(input("What is the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is {area}m^2")

"""
create a script that  will ask the user for a single task, its priority level, and if it is time-sensitive. The program will then provide a customized reminder for that task, demonstrating control flow and loops without relying on data structures to store multiple tasks.
Instructions:
1.	Prompt for a Single Task:
o	Ask the user to input a task description and save it into a task variable
o	Prompt for the task’s priority (high, medium, low) and save it into a priority variable
o	In a time_bound variable, Ask if the task is time-bound (yes or no)
2.	Process the Task Based on Priority and Time Sensitivity:
o	Use a Match Case statement to react differently based on the task’s priority.
o	Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
3.	Provide a Customized Reminder:
o	Print a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity.
o	A message should be ‘that requires immediate attention today!’
"""
task = input("What is your task?: ")
description = input("What is the description of your task: ")
priority = input("what is the priority level of the task?: ").lower()
time_bound = input("Is the task time-bound (Yes or No)?: ").lower()
match priority:
    case "high":
        if time_bound == "yes":
            print(f"The task {task} is high and has a time bound")
        elif time_bound == "no":
            print(f"The task {task} is high but does not have a time bound")
        else:
            print("Wrong input time bound")
    case "medium":
        if time_bound == "yes":
            print(f"The task {task} is medium and has a time bound")
        elif time_bound == "no":
            print(f"The task {task} is medium but does not have a time bound")
        else:
            print("Wrong input time bound")
    case "low":
        if time_bound == "yes":
            print(f"The task {task} is low and has a time bound")
        elif time_bound == "no":
            print(f"The task {task} is low but does not have a time bound")
        else:
            print("Wrong input time bound")
    case _:
        print("Invalid priority entry")

"""
Create a script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).
Instructions:
o	Ask the user to input a positive integer that represents the size of the pattern (i.e., the length of each side of the square): Enter the size of the pattern:.
o	First, use a while loop to iterate through each row of the pattern.
o	Inside the while loop, use a for loop to print asterisks () side by side without advancing to a new line (you can use print("", end="") for this).
o	After completing each row, print a newline character to move to the next row.
o	Continue until the pattern forms a square of the inputted size.
""" 
size = int(input("What is the size of the square: "))
count = 0
while count < size:
    for j in range(size):
        print("*", end="")
    count += 1
    print()