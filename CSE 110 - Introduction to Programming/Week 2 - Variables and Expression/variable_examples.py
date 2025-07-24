"""# Prompt the user for their age. 
# Convert it to a number, add one to it, 
# and tell them how old they will be on their next birthday.
age = input("How old are you? ")
age = int(age)
print(f"On your next birthday, you will be {age + 1}")

#Prompt the user for the number of egg cartons they have. 
# Assume each carton holds 12 eggs, multiply their number by 12, 
# and display the total number of eggs.
cartons_number = int(input("How many egg cartons do you have? "))
eggs = cartons_number * 12
print(f"You have {eggs} eggs.")


#Prompt the user for a number of cookies and a number of people. 
# Then, divide the number of cookies by the number of people to 
# determine how many cookies each person gets.

cookies_number = float(input("How many cookies do you have? "))
people_number = int(input("How many people are there? "))
person = cookies_number / people_number
print(f"Each person may have {person} cookies")

#Write a program to convert from Fahrenheit to Celsius. 
# Display the result to one decimal place of precision.

#To convert degrees in Fahrenheit to Celsius 
# you need to subtract 32 from the Fahrenheit amount 
# and then multiply it by the fraction 5/9.
fahrenheit = float(input("What is the temperature in Fahrenheit? "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"The temperature is Celsius is {celsius:.1f} degrees.")"""
x = 5
x =+ 1
print(x)