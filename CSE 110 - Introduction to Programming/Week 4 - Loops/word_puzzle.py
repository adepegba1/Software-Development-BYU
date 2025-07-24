"""
The program contains a hidden secret word stored in a variable. 
This word can have any number of letters in it. 
When the program runs, the user is shown underscores ( _ ) for each letter of the word.

The user then enters a guess. If the guess is correct, the user wins and the game is over.
If the guess is not correct, the user will be given a hint to help them improve their guess for the next round.

The game continues prompting the user for new guesses and showing them hints until they guess the word correctly.
When the game is over, the program displays the number of guesses that were made.

The guess must be the same number of letters as the secret word. 
If the guess has a different numbers of letters, 
the user is given a message explaining this, and no hint is provided.

The hint shows the letters of the guess, but each letter is rendered in a special way as follows:
An underscore _ indicates that the letter was not present in the secret word.
A lowercase letter indicates that the letter was present somewhere in the secret word, but not at that position.
An uppercase letter indicates that the letter was present at that exact spot in the secret word. 
(In other words, if the second letter in the guess is also the second letter in the secret word, then that letter is shown as a capital.)

After winning the game, the user is ask if he will like to continue with the game.
"""
import random
print("Welcome to the word guessing game!")
keep_playing = "yes"
while keep_playing.lower() == "yes":
    # The user has the 3 options to guess a name or the default guess 
    choice = input("What choice did you want to guess name: animal, country, colour: ")
    animal = ["Dog", "Fish", "Elephant", "Tiger", "Monkey"]
    country = ["Nigeria", "United State", "Turkey", "China", "Denmark"]
    colour = ["Blue", "Yellow", "Red", "Purple", "Green"]
    # Check the user choice of guessing name
    if choice.lower() == "animal":
        secret = random.choice(animal).lower()
    elif choice.lower() == "country":
        secret  = random.choice(country).lower()
    elif choice.lower() == "colour":
        secret = random.choice(colour).lower()
    else:
        secret = "Mosiah".lower()
    # Get the length of the secret word and multiply it by underscore
    secret_len = len(secret) * "_ "
    # Guess counter initialize
    count = 0
    # guess intialize
    guess = ""
    # checking that guess and secret name are not the same.
    while guess.lower() != secret.lower():
        # printing out the number of guess the user is expected to enter
        print(f"\nYour guess is {secret_len}")
        # Asking the user what there guess is
        guess = input("What is your guess? \n").lower()
        # incrementing the count of guesses
        count += 1
        # The hint is intailize here 
        hint = ""
        # Checking the length of the guess word
        if len(guess) != len(secret):
            print("Sorry, the guess must have the same number of letters as the secret word")
        # if the len are the same, it will perform the code below
        else:
            # intialize the index of the variable
            index = 0  
            # looping through the guess letter          
            for i in guess:
                # if the guess letter is in secert
                if i in secret:
                    # if it is in same position make it uppercase
                    if guess[index] == secret[index]:
                        hint = hint + i.upper()
                    # if it not same position but in the secret word, make it lowercase
                    else:
                        hint = hint + i.lower()
                # if the letter is not in the secret word, print underscore 
                else:
                    hint = hint + ("_ ")
                # increase the index by 1
                index += 1
            # print the output of the guess hint to the user
            else:
                print(f"Your guess hint is {hint}")
    print(f"\nYou won! The word was {secret.title()}")
    print(f"Number of guesses is {count}")
    keep_playing = input("\nWould you like to play again(yes/no)?: ")
print("Thank you for playing!!!")