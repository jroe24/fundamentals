import random

# computer_wins = 0
# user_wins = 0

# while (computer_wins <3 or player_wins < 3):
user_input = input("Choose your weapon (rock, paper, scissors): ")
weapon = ["rock", "paper", "scissors"]
computer_input = random.choice(weapon)
print(f"You chose {user_input}, Computer chose {computer_input}.")

if user_input == computer_input:
    print(f"You both chose {user_input}, You tied!")
elif user_input == "paper":
    if computer_input == "rock":
        print("Paper covers rock! You win!")
        # user_wins += 1
    else:
        print("Scissors cuts paper! You lose.")
        # computer_wins =+ 1
elif user_input == "rock":
    if computer_input == "scissors":
        print("Rock crushes scissors! You win!")
        # user_wins =+ 1
    else:
        print("Paper covers rock! You lose.")
        # computer_wins =+ 1
elif user_input == "scissors":
    if computer_input == "paper":
        print("Scissors cuts paper! You win!")
        # user_wins =+ 1
    else:
        print("Rock smashes scissors! You lose.")
        # computer_wins =+ 1
