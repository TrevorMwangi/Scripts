import random

user_wins = 0
computer_wins = 0
tied_games = 0

options = ["rock", "paper", "scissors"]

def print_stats():
    print("Current Stats:")
    print("You won", user_wins, "time" if user_wins == 1 else "times")
    print("The computer won", computer_wins, "time." if computer_wins == 1 else "times.")
    print("The game was tied", tied_games, "time." if tied_games == 1 else "times.")
    print()

while True:
    user_input = input("Type Rock/Paper/Scissors, Stats to check statistics, or Q to quit: ").lower()
    
    if user_input == "q":
        break
    
    if user_input == "stats":
        print_stats()
        continue

    if user_input not in options:
        print("Invalid input! Please try again.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        print()
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        print()
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        print()
        user_wins += 1

    elif user_input == computer_pick:
        print("It's a tie!")
        print()
        tied_games += 1

    else:
        print("You lost!")
        print()
        computer_wins += 1

print_stats()
print("Goodbye!")
