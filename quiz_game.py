print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay lets play!")

#question 1
answer = input("What is the capital city of Kenya? ")
if answer == "Nairobi":
    print("Correct!")
else:
    print("Incorrect")
    print("Try again!")

#question 2
answer = input("Who wrote the 48 Laws of Power? ")
if answer == "Robert Greene":
    print("Correct!")
else:
    print("Incorrect")
    print("Try again!")

#question 3
answer = input("In Greek mythology, who is the god of thunder? ")
if answer == "Zeus":
    print("Correct!")
else:
    print("Incorrect")
    print("Try again!")

#question 4
answer = input("Which famous scientist developed the theory of general relativity? ")
if answer == "Albert Einstein":
    print("Correct!")
else:
    print("Incorrect")
    print("Try again!") 