"""
An ID badge, such as a drivers license or student ID, 
contains personal details that are formatted in a very specific way.
For this activity you will write a program that will 
create a properly formatted ID badge.
"""

print("Please enter the following information: ")
First_name = input("What is your first name? ")
Last_name = input("What is your last name? ")
Email_address = input("Your email address? ")
Phone_number = input("Your phone number? ")
Job_title  = input("What is your job title? ")
ID_number = input("What is your ID number? ")
# Printing the details out
print("The card is:")
print("----------------------------------------------------")
print(f"{Last_name.upper()} , {First_name.capitalize()}")
print(f"{Job_title.title()}")
print(ID_number)
print()
print(Email_address.lower())
print(Phone_number)
print("-----------------------------------------------------")
