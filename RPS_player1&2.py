# Two player, Rock/Paper/Scissors

user1_wins = 0
user2_wins = 0
draws = 0

Player_1 = input("What is you name player 1?  ")
Player_2 = input("What is your name player 2?  ")

options = ["rock", "paper", "scissors"]

while True:
    user1_input = input(Player_1,( "type Rock/Paper/Scissors or Q to quit: ")).lower()
    if user1_input == "q":
        break

    if user1_input not in options:
        print("Invalid input. Please try again.")
        continue

    user2_input = input(Player_2, "type Rock/Paper/Scissors or Q to quit: ").lower()
    print()
    if user2_input == "q":
        break

    if user2_input not in options:
        print("Invalid input. Please try again.")
        continue

    print(Player_1, "picked", user1_input + ".")
    print(Player_2, "picked", user2_input + ".")
    print()

    if (
        (user1_input == "rock" and user2_input == "scissors")
        or (user1_input == "paper" and user2_input == "rock")
        or (user1_input == "scissors" and user2_input == "paper")
    ):
        print(Player_1, "wins!")
        print("Go again!!")
        print()
        user1_wins += 1

    elif (
        (user2_input == "rock" and user1_input == "scissors")
        or (user2_input == "paper" and user1_input == "rock")
        or (user2_input == "scissors" and user1_input == "paper")
    ):
        print(Player_2, "wins!")
        print("Go again!!")
        print()
        user2_wins += 1

    else:
        print("It's a tie!")
        print()
        draws += 1

print(Player_1, "won", user1_wins, "times.")
print(Player_2, "won", user2_wins, "times.")
print("The game was tied", draws ,"times.")
print("Goodbye!")
