import random
target = random.randint(1, 100)
attempts = 0
while True:
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
