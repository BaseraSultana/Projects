# Guess the Number

A simple command-line number guessing game written in Python. The game picks a number from 1 to 100, and you try to guess it using the hints provided.

## Features

- Randomly selects a target number between 1 and 100
- Tells you whether each guess is higher or lower than the target
- Counts valid guesses and reports how many you needed
- Handles non-numeric input without ending the game
- Lets you quit at any time by entering `Q`

## Requirements

- Python 3.x

## How to Run

Open a terminal in the project folder and run:

```bash
python main.py
```

On Windows, you can also use:

```powershell
py main.py
```

## How to Play

1. Run the program.
2. Enter a whole number from 1 to 100.
3. Use the hint to make your next guess higher or lower.
4. Keep guessing until you find the target.
5. Enter `Q` to quit before finding the number.

The game ends when you guess correctly or quit. It then displays a game-over message.

## Example

```text
Guess a number between 1 to 100 or Quit(Q) : 50
Your guess is less than the target!

Guess a number between 1 to 100 or Quit(Q) : 75
Your guess is greater than the target!

Guess a number between 1 to 100 or Quit(Q) : 63
Congratulations! You guessed the number in 3 guesses.

--------GAME OVER--------
```

The target is random, so the hints and example guesses will vary each time you play.

## Future Improvements

- Add difficulty levels with different number ranges
- Limit the number of guesses for a challenge mode
- Ask whether the player wants to start another round
- Track and display the best (fewest) number of guesses
- Add input validation so guesses outside 1 to 100 receive a helpful message
- Add automated tests for game behavior

## Project Structure

```text
GUESS_THE_NUMBER/
├── main.py
└── README.md
```