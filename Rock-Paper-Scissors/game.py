import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

while True:

    user_choice = input("Please choose rock, paper, or scissors:(q to quit): ").lower()

    if user_choice == "q":
        print("Final Score:")
        print("Your score:", user_score)
        print("Computer score:", computer_score)
        print("Thanks for playing! Goodbye.")
        break

    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")

    elif user_choice == "rock" and computer_choice == "paper":
        print("You lost.")
        computer_score += 1

    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        user_score += 1

    elif user_choice == "paper" and computer_choice == "scissors":
        print("You lost.")
        computer_score += 1

    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        user_score += 1

    elif user_choice == "scissors" and computer_choice == "rock":
        print("You lost.")
        computer_score += 1

    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        user_score += 1

if user_score > computer_score:
    print("You are the winner!")

elif user_score < computer_score:
    print("Computer is the winner!")

else:
    print("The game is a draw!")
