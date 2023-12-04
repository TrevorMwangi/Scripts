try:
    # Get user input as an integer
    user_input = int(input("Enter a number: "))

    # Check if the input is a multiple of 5
    if user_input % 5 == 0:
        print(f"{user_input} is a multiple of 5.")
    else:
        print(f"{user_input} is not a multiple of 5.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
