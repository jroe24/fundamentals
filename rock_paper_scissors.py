import random

user_input = input("Choose your weapon (rock, paper, scissors): ")
weapon = ["rock", "paper", "scissors"]
computer_input = random.choice(weapon)
print(f"You chose {user_input}, Computer chose {computer_input}.")

if user_input == computer_input:
    print(f"You both chose {user_input}, You tied!")
elif user_input == "paper":
    if computer_input == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_input == "rock":
    if computer_input == "scissors":
        print("Rock crushes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_input == "scissors":
    if computer_input == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")