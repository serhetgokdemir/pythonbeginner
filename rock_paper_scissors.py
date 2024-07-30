import random

list = ["rock","paper","scissors"]
print("rock = 1 ||||||| paper = 2 ||||||| scissors = 3")

1, 2, 3 == "rock","paper","scissors"
while True:

    computer_choice = random.choice(list)
    user_choice = int(input("Enter 1, 2 or 3: "))
    print("Rock...Paper...Scissors!")
    print("...")
    print("...")

    print(f"{computer_choice}")
    if user_choice == 1:
        if computer_choice == "rock":
            print("Draw.")
        elif computer_choice == "paper":
            print("You lost.")
        elif computer_choice == "scissors":
            print("You win.")

    elif user_choice == 2:
        if computer_choice == "paper":
            print("Draw.")
        elif computer_choice == "rock":
            print("You win.")
        elif computer_choice == "scissors":
            print("You lost.")


    elif user_choice == 3:
        if computer_choice == "scissors":
            print("Draw.")
        elif computer_choice == "rock":
            print("You lost.")
        elif computer_choice == "paper":
            print("You win.")

