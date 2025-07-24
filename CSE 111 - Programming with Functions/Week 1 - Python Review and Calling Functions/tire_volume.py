"""
Write a program that will accept user input that describes a tire 
then calculate and display the tire's volume. 
Record the tire information in a log file.

Have the user enter a tire width in mm.
Have the user enter the aspect ratio.
Have the user enter the diameter of the wheel in inches.
Calculate and display the tire's volume.
Log the information in a text file.
current date (Do NOT include time)
width of the tire
aspect ratio of the tire
diameter of the wheel
volume of the tire (rounded to two decimal places)

After your program prints the tire volume to the terminal window,
The program should ask the user if they wants to buy tires with the dimensions that they entered. 
If the user answers “yes”, the program ask for the user name, phone number and 
store the information in the volumes.txt file.
"""
# importing the library to use for the program to work effectively
import math
import datetime

# Asking the user the width, aspect ratio and diameter of tire
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter= int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculating the volume of the tire
volume = math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + (2540 * diameter)) / 10000000000

# Printing the volume of the tire out to the user
print(f"The approximate volume is {volume:.2f} liters\n")

# Asking the user if they are interested in buying the tire
user_decision = input("Will you wants to buy tires with the dimensions that you entered (Yes or No): ")

# if the user is interested in the tire, the program as for the information of the user
if user_decision.lower() == "yes":
    name = input("What is your name: ")
    phone_number = input("What is your phone number: ")

# Getting the current date with the library of datetime and using the today function
current_date = datetime.date.today()

# Opening the text file to save the result of the parameter that is entered by the user
with open("volumes.txt", "a") as volume_file:

    # if the user type yes to purchase the tire, the information is save in the text file
    if user_decision.lower() == "yes":        
        print(f"Customer name: {name.title()}, Phone number: {phone_number}, {current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}", sep=", ", file= volume_file)

    # If the user did not want to buy the tire, only the information the of the tire is save in the text file
    else:
        print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}", sep=", ", file= volume_file)
    
