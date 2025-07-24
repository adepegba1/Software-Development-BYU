"""
In a text-based adventure game, 
the user is presented a scenario with different options. 
Depending on the option they choose, they have different consequences, 
which in turn present different choices for the next action.
For any wrong input, the program end.
The user can also quit the game using the QUIT keyword

"""

print("""You find yourself at the entrance of a mysterious forest. The path splits in two directions.
Type LEFT to take the path to the left or RIGHT to take the path to the right""")
direction = input("Your direction? LEFT or RIGHT: ")
if direction.lower() == "left":
    print("""\nYou encounter a sparkling stream blocking your way
Type CROSS to attempt to cross the stream or FOLLOW to follow the stream downstream
or QUIT to quit the game""")
    action = input("What do you want to do? CROSS or FOLLOW or QUIT: ")
    if action.lower() == "cross":
        print("""\nThe stream is deeper than it looks and you struggle to cross.
Type SWIM to swim across or TURN BACK to turn back and find another way
or QUIT to quit the game""")
        action_2 = input("What do you want to do? SWIM or TURN BACK or QUIT: ")
        if action_2.lower() == "swim":
            print("""\nYou have successfully swim across and find a hidden treasure chest
Type OPEN CHEST to open the chest or LEAVE CHEST to leave the chest and continue your journey.
or QUIT to quit the game""")
            action_3 = input("What do you want to do? OPEN CHEST or LEAVE CHEST or QUIT: ")
            if action_3.lower() == "open chest":
                print("""\nCongratulation!, You found the Treasure!!!
You have completed the Adventure Quest.
Thank you for playing!""")
            elif action_3.lower() == "leave chest":
                print("""\nYou did not find the Treasure.
Please try again next time
Thank you for playing!""")
            elif action_3.lower() == "quit":
                print("You quit the game!")
            else:
                print("\nYou enter the wrong command!!!")
        elif action_2.lower() == "turn back":
            print("""\nYou find a hidden oath that leads to a secret garden
Type ENTER GARDEN to enter the garden or LEAVE GARDEN to leave the garden and continue your journey
or QUIT to quit the game""")
            action_3 = input("What do you want to do? ENTER GARDEN or LEAVE GARDEN or QUIT: ")
            if action_3.lower() == "enter garden":
                print("""\nCongratulation!, You found the Treasure!!!
You have completed the Adventure Quest.
Thank you for playing!""")
            elif action_3.lower() == "leave garden":
                print("""\nYou did not find the Treasure.
Please try again next time
Thank you for playing!""")
            elif action_3.lower() == "quit":
                print("You quit the game!")
            else:
                print("\nYou enter the wrong command!!!")
        elif action_2.lower() == "quit":
            print("You quit the game!")
        else:
            print("\nYou type the wrong command!!!")
    elif action.lower() == "follow":
        print("""\nThe stream leads you to a waterfall
Type CLIMB to climb the waterfall or EXPLORE to explore the area around the waterfall
or QUIT to quit the game""")
        action_2 = input("What do you want to do? CLIMB or EXPLORE or QUIT: ")
        if action_2.lower() == "climb":
            print("""\nYou climb the waterfall and discover a hidden cave
Type ENTER CAVE to enter the cave or LEAVE CAVE to leave the cave and continue the journey
or QUIT to quit the game""")
            action_3 = input("What do you want to do? ENTER CAVE or LEAVE CAVE or QUIT: ")
            if action_3.lower() == "enter cave":
                print("""\nCongratulation!, You found the Treasure!!!
You have completed the Adventure Quest.
Thank you for playing!""")
            elif action_3.lower() == "leave cave":
                print("""\nYou did not find the Treasure.
Please try again next time
Thank you for playing!""")
            elif action_3.lower() == "quit":
                print("You quit the game!")
            else:
                print("You type the wrong command!")

        elif action_2.lower() == "explore":
            print("""\nYou find a hidden path that leads to a migical glade
Type ENTER GLADE to enter the glade or LEAVE GLADE to leave the glade and continue your journey
or QUIT to quit the game""")
            action_3 = input("What do you want to do? ENTER GLADE or LEAVE GLADE or QUIT: ")
            if action_3.lower() == "enter glade":
                print("""\nCongratulation!, You found the Treasure!!!
You have completed the Adventure Quest.
Thank you for playing!""")
            elif action_3.lower() == "leave glade":
                print("""\nYou did not find the Treasure.
Please try again next time
Thank you for playing!""")
            elif action_3.lower() == "quit":
                print("You quit the game!")
            else:
                print("\nYou enter the wrong command!!!")
        elif action_2.lower() == "quit":
            print("You quit the game!")
        else:
            print("\nYou type the wrong command!!!")
    elif action.lower() == "quit":
        print("You quit the game!")
    else:
        print("\nYou type the wrong command!!!")
elif direction.lower() == "right":
    print("""\nYou come across a dark cave entrance
Type ENTER to enter the cave or CONTINUE to continue along the path or QUIT to quit the game""")
    action = input("What do you want to do? ENTER or CONTINUE or QUIT: ")
    if action.lower() == "enter":
        print("""\nThe cave is dark and damp
Type LIGHT to light a torch and proceed or EXIT to exit the cave and return to the forest.
or QUIT to quit the game""")
        action_2 = input("What do you want to do? LIGHT or EXIT or QUIT: ")
        if action_2.lower() == "light":
            print("""\nThe tourch reveals a hidden passage
Type ENTER PASSAGE to enter the passage or LEAVE PASSAGE to leave the passage and continue your journey
or QUIT to quit the game""")
            action_3 = input("What do you want to do? ENTER PASSAGE or LEAVE PASSAGE or QUIT")
            if action_3.lower() == "enter passage":
                print("""\nCongratulation!, You found the Treasure!!!
You have completed the Adventure Quest.
Thank you for playing!""")
            elif action_3.lower() == "leave passage":
                print("""\nYou did not find the Treasure.
Please try again next time
Thank you for playing!""")
            elif action_3.lower() == "quit":
                print("You quit the game!")
            else:
                print("\nYou enter the wrong command!!!")
        elif action_2.lower() == "exit":
            print("""\nYou return to the forest and find a hidden path
Type FOLLOW PATH to follow the path or LEAVE PATH to leave the path and continue your journey
or QUIT to quit the game""")
            action_3 = input("What do you want to do? FOLLOW PATH or LEAVE PATH or QUIT: ")
            if action_3.lower() == "follow path":
                print("""\nCongratulation!, You found the Treasure!!!
You have completed the Adventure Quest.\nThank you for playing!""")
            elif action_3.lower() == "leave path":
                print("""\nYou did not find the Treasure.
Please try again next time\nThank you for playing!""")
            elif action_3.lower() == "quit":
                print("You quit the game!")
            else:
                print("\nYou enter the wrong command!!!")
        elif action_2.lower() == "quit":
            print("You quit the game!")
        else:
            print("\nYou type the wrong commmand!!!")
    elif action.lower() == "continue":
        print("""\nThe path leads you to a clearing with a mysterious door
Type OPEN  to open the door or LEAVE to leave the door and continue exploring
or QUIT to quit the game""")
        action_2 = input("What do yo want to do? OPEN or LEAVE or QUIT: ")
        if action_2.lower() == "open":
            print("""\nThe door opens to reveal a hidden chamber
Type ENTER CHAMBER to enter the chamber or LEAVE CHAMBER to leave the chamber and contiue your journey
or QUIT to quit the game""")
            action_3 = input("What do you want to do? ENTER CHAMBER or LEAVE CHAMBER or QUIT: ")
            if action_3.lower() == "enter chamber":
                print("""\nCongratulation!, You found the Treasure!!!
You have completed the Adventure Quest.\nThank you for playing!""")
            elif action_3.lower() == "leave chamber":
                print("""\nYou did not find the Treasure.
Please try again next time\nThank you for playing!""")
            elif action_3.lower() == "quit":
                print("You quit the game!")
            else:
                print("\nYou enter the wrong command!!!")
        elif action_2.lower() == "leave":
            print("""\nYou continue exploring and find a hidden treasure
Type TAKE TREASURE to take the treasure or LEAVE TREASURE to leave the treasure and continue your journey
or QUIT to quit the game""")
            action_3 =input("What do you want to do? TAKE TREASURE or LEAVE TREASURE or QUIT: ")
            if action_3.lower() == "take treasure":
                print("""\nCongratulation!, You found the Treasure!!!
You have completed the Adventure Quest.\nThank you for playing!""")
            elif action_3.lower() == "leave treasure":
                print("""\nYou did not find the Treasure.
Please try again next time\nThank you for playing!""")
            elif action_3.lower() == "quit":
                print("You quit the game!")
            else:
                print("\nYou enter the wrong command!!!")
        elif action_2.lower() == "quit":
            print("You quit the game!")
        else:
            print("\nYou type the wrong command!!!")
    elif action.lower() == "quit":
        print("You quit the game!")
    else:
        print("\nYou type the wrong command!!!")
else:
    print("\nYou type the wrong command\nTry again!!!")
print("\nYour choices have led you on a unique journey")
