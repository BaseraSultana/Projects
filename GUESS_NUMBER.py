import random
target = random.randint(1, 100)
# Attempts is used to count the number of times the user guessed.
attempts = 0

# This is a number guessing game. Designed for the users to spend their time doing something interesting.
while True:
    # Guess is the input provided by the user for guessing the actual number.

    guess = input("\n Guess a number between 1 to 100 or Quit(Q) : ").strip()

    if (guess.casefold() == "q"):
        print("\n You have Quit the game!")
        break

    try:
        guess = int(guess)
    except ValueError:
        print("Invalid Input. Try again!")
        continue

    attempts += 1

    if (guess == target):
        print(
            f"\n Congratulations! You guessed the number in {attempts} guesses.")
        break
    elif guess > target:
        print("Your guess is greater than the target!")
    else:
        print("Your guess is less than the target!")

print("\n--------GAME OVER--------")
