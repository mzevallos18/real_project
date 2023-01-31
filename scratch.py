import random

play_again = 'yes'
while play_again == 'yes':
    # Generate a random number between 1 and 100
    answer = random.randint(1, 100)

    # Ask the user to guess the number
    guess = int(input("Guess a number between 1 and 100: "))

    # Keep track of the number of guesses
    guesses = 1

    # Loop until the user guesses the correct number
    while guess != answer:
        if guess < answer:
            print("Too low!")
        else:
            print("Too high!")
        guess = int(input("Guess again: "))
        guesses += 1

    # Print a message when the user guesses the correct number
    print("Congratulations! You guessed the correct number in", guesses, "tries.")
    play_again = input("Do you want to play again (yes or no)? ")
