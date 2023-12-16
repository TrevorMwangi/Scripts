print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay lets play!")

#question 1
answer = input("What is the capital city of Kenya? ")
if answer.lower() == "nairobi":
    print("Correct!")
else:
    print("Incorrect")
    print("Try again!")

#question 2
answer = input("Who wrote the 48 Laws of Power? ")
if answer.lower() == "robert greene":
    print("Correct!")
else:
    print("Incorrect")
    print("Try again!")

#question 3
answer = input("In Greek mythology, who is the god of thunder? ")
if answer.lower() == "zeus":
    print("Correct!")
else:
    print("Incorrect")
    print("Try again!")

#question 4
answer = input("Which famous scientist developed the theory of general relativity? ")
if answer.lower() == "albert einstein":
    print("Correct!")
else:
    print("Incorrect")
    print("Try again!") 