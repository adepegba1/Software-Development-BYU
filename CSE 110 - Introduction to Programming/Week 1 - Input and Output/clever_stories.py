"""
For this assignment, you will implement a program that asks the user
 for a series of words and then displays the story with the user's 
 words inserted into the appropriate places.

The program should begin by asking the user for
 each of the words. It should then, fill those words into 
 the appropriate places in the story.
"""
# Asking the user for inputs
print("Please enter the following: ")
adjective = input("What is the adjective of the story? ")
animal = input("Which animal did your story have? ")
verb_1 = input("What is the verb of your story? ")
exclamation = input("What is the exclamation of your story? ")
verb_2 = input("What is another verb for your story? ")
verb_3 = input("What is the last verb for your story? ")

# printing the story out
print("Your story is: ")
print()
print(f"The other day, I was really in trouble. It all started when I saw a very")
print(f"{adjective.lower()} {animal.capitalize()} {verb_1.lower()} down the hallway. \"{exclamation.capitalize()}!\" I yelled. But all")
print(f"I could think to do was to {verb_2.lower()} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {verb_3.lower()}")
print(f"right in front of my family.")
