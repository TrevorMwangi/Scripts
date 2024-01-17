user1_wins = 0
user2_wins = 0
draws = 0

Player_1 = input("What is your name, player 1? ")
Player_2 = input("What is your name, player 2? ")

options = ["rock", "paper", "scissors"]

while True:
    user1_input = input("{} type Rock/Paper/Scissors or Q to quit: ".format(Player_1)).lower()
    if user1_input == "q":
        break

    if user1_input not in options:
        print("Invalid input. Please try again.")
        continue

    user2_input = input("{} type Rock/Paper/Scissors or Q to quit: ".format(Player_2)).lower()
    print()
    if user2_input == "q":
        break

    if user2_input not in options:
        print("Invalid input. Please try again.")
        continue

    print("{} picked {}".format(Player_1, user1_input))
    print("{} picked {}".format(Player_2, user2_input))
    print()

    if (
        (user1_input == "rock" and user2_input == "scissors")
        or (user1_input == "paper" and user2_input == "rock")
        or (user1_input == "scissors" and user2_input == "paper")
    ):
        user1_wins += 1
        print("{} wins{}!".format(Player_1, "" if user1_wins == 1 else " {} times".format(user1_wins)))
        print("Go again!!")
        print()

    elif (
        (user2_input == "rock" and user1_input == "scissors")
        or (user2_input == "paper" and user1_input == "rock")
        or (user2_input == "scissors" and user1_input == "paper")
    ):
        user2_wins += 1
        print("{} wins{}!".format(Player_2, "" if user2_wins == 1 else " {} times".format(user2_wins)))
        print("Go again!!")
        print()

    else:
        draws += 1
        print("It's a tie!")
        print()

print("{} won {}.".format(Player_1, "1 time" if user1_wins == 1 else "{} times".format(user1_wins)))
print("{} won {}.".format(Player_2, "1 time" if user2_wins == 1 else "{} times".format(user2_wins)))
print("The game was tied {}.".format("1 time" if draws == 1 else "{} times".format(draws)))
print("Goodbye!")
