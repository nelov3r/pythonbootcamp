name = input("Please enter your name!")

print(f"Greetings {name}, My Name is FUCKING ALF! WELCOME TO MY TREASURE GAME!!!!")
print("Your goal is find a Treasure!")

choice1 = input(
    'You\'re at a crossroad, where do u wanna go ? Type "left" or "right".'
).lower()

if choice1 == "left":
    choice2 = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across faster.'
    ).lower()
    if choice2 == "wait":
        choice3 = input(
            "You arrive at the isaland unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do u choose ?"
        ).lower()
        if choice3 == "red":
            print("This room is full of fire! GAME OVER!")
        elif choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "blue":
            print("This room is full of water! GAME OVER!")
    else:
        print("You have been attacked by an angry shark. GAME OVER!!!!")
else:
    print("The monster killed u on that way. GAME OVER!!!!!")
