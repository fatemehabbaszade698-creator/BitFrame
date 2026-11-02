import random 

while(True):
    number = random.randint(1 , 100)
    print("I chose a number between 1 and 100.")
    count = 0

    while True:

        try:

            Guess = int(input("Please enter your guess: "))

            if Guess <= 1 or Guess >= 100:
                print("Please enter a number between 1 and 100.")
                continue

            count +=1

            if Guess > number:
                print("Too high, try a smaller number.")

            elif Guess < number:
                print("Too low, try a bigger number.")

            else:
                print("Correct! You did it!!!!!!!!!!!!!!!!!!!!!!.")
                print("Number of counts:", count)
                break

        except ValueError:
            print("Please enter a valid number.")

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break





