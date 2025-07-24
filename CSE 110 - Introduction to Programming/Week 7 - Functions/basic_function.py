"""
Write three functions:

display_regular—Receives a string and prints it out, exactly as received.

display_uppercase—Receives a string, converts it to upper case, and then prints it out.

display_lowercase—Receives a string, converts it to lower case, and then prints it out.
"""
def display_regular(message):
    print(message)

def display_uppercase(message):
    print(message.upper())

def display_lowercase(message):
    print(message.lower())

word = input('What is your message? ')
print()
display_regular(word)
display_lowercase(word)
display_uppercase(word)