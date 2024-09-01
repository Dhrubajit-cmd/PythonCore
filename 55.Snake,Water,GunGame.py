# Let's start

import random
def computer_choice() :
    choices = ["snake","water","gun"]
    return random.choice(choices)
intro = "SNAKE-WATER-GUN"
intro_center = intro.center(100,".")
print(intro_center)
rounds = int(input("Enter the number of rounds you want to play: \n"))
for i in range(rounds):
 comp_choice = computer_choice()
 user_choice = input("Enter your choice:\n")
 if user_choice == comp_choice :
    print(f"Computer's choice is: {user_choice}.\n")
    print("Draw.\n")
 elif user_choice == "snake" and comp_choice == "water":
    print("Computer's choice is: water.\n")
    print("You Win.\n")
 elif user_choice == "snake" and comp_choice == "gun" :
    print("Computer's choice is: gun.\n")
    print("You Lose.\n")
 elif user_choice == "water" and comp_choice == "gun" :
    print("Computer's choice is: gun.\n")
    print("You Win.\n")
 elif user_choice == "water" and comp_choice== "snake" :
    print("Computer's choice is: snake.\n")
    print("You Lose.\n")
 elif user_choice == "gun" and comp_choice == "snake" :
    print("Computer's choice is: snake.\n")
    print("You Win.\n")
 elif user_choice == "gun" and comp_choice == "water" :
    print("Computer's choice is: water.\n")
    print("You Lose.\n")
 elif user_choice == "exit" :
    break
 elif user_choice == "quit" :
    break
 else :
     print("Invalid Input. \n")
extro = "Thank you for playing."
extro_center = extro.center(100,".")
print(extro_center)

# The End of the CODE
