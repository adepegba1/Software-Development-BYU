# Guess my number game
import random

replay = "yes"
while replay.lower() == "yes":
    number = random.randint(1,100)
    count = 0 
    guess = 0
    while number != guess:
        guess = int(input("\nWhat is your guess: "))
        if guess > number :
            print("Guess lower number")
        elif guess < number:
            print("Guess higher number")
        else:
            print("You guessed it!")
        count = count + 1
    print(f"It took you {count} guesses")
    replay = input("Would you like to play again (yes/no)? ")
print("Thank you for playing. Goodbye.")

        

