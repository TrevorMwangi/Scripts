# Two player, Rock/Paper/Scissors

user1_wins = 0
user2_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user1_input = input("Player 1, type Rock/Paper/Scissors or Q to quit: ").lower()
    if user1_input == "q":
        break

    if user1_input not in options:
        print("Invalid input. Please try again.")
        continue

    user2_input = input("Player 2, type Rock/Paper/Scissors or Q to quit: ").lower()
    if user2_input == "q":
        break

    if user2_input not in options:
        print("Invalid input. Please try again.")
        continue

    print("Player 1 picked", user1_input + ".")
    print("Player 2 picked", user2_input + ".")

    if (
        (user1_input == "rock" and user2_input == "scissors")
        or (user1_input == "paper" and user2_input == "rock")
        or (user1_input == "scissors" and user2_input == "paper")
    ):
        print("Player 1 wins!")
        print()
        user1_wins += 1

    elif (
        (user2_input == "rock" and user1_input == "scissors")
        or (user2_input == "paper" and user1_input == "rock")
        or (user2_input == "scissors" and user1_input == "paper")
    ):
        print("Player 2 wins!")
        print()
        user2_wins += 1

    else:
        print("It's a tie!")
        print()

print("Player 1 won", user1_wins, "times.")
print("Player 2 won", user2_wins, "times.")
print("Goodbye!")
