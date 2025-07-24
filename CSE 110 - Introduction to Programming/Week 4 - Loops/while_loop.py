"""
Use a while loop to ask the user for a positive number (>= 0). 
Continue asking as long as the number is negative, then display the number.
"""
number = int(input("Please type a positive number: "))
while number < 0:
    print("Sorry that is a negative number.", end="")
    print("Please try again.")
    number = int(input("Please enter a positive number: "))
print(f"The number is : {number}" )

"""
Use a while loop, to simulate a child asking their parent for a piece of candy. 
Have the program keep looping until the user answers "yes", then have the program output "Thank you.
"""
answer = "no"
while answer != "yes":
    answer = input("May I have a candy? ")
print("Thank you.")
