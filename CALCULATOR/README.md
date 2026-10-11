# Calculator Project

A simple command-line calculator built in Python. It allows users to perform common arithmetic operations, view calculation history, and continue using the calculator until they choose to exit.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Modulus
- Exponentiation
- Floor division
- Calculation history
- Menu-driven interaction

## Project Structure

```text
CALCULATOR/
├── main.py
└── README.md
```

## Requirements

- Python 3.x

## How to Run

From the project folder, run:

```bash
python main.py
```

## How It Works

When the program starts, it displays a calculator menu with options such as:

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Exponent
7. Floor Division
8. History
9. Exit

You can select an operation by entering its number, then provide the required values when prompted. After each calculation, the program asks whether you want to continue or exit.

## Example

```text
CALCULATOR MENU
1. ADDITION
2. SUBTRACTION
3. MULTIPLICATION
4. DIVISION
5. MODULUS
6. EXPONENT
7. FLOOR DIVISION
8. HISTORY
9. EXIT
Enter Your Choice: 1
Enter the First number: 10
Enter the Second number: 5
Result = 15.00
Do You Want To Continue?
1. Yes
2. No
```

## Notes

- Division by zero is handled gracefully with a "Not defined" message.
- The program stores calculation history during the current session.
- Invalid menu input displays an error message and prompts the user to try again.

## Future Improvements

The calculator can be expanded with several useful enhancements, including:

- Saving calculation history to a file so it remains available after the program closes
- Adding a graphical user interface (GUI) for easier interaction
- Improving input validation for invalid or unexpected user entries
- Supporting more advanced operations such as square root, logarithms, and trigonometric functions
- Adding unit tests to improve reliability and maintainability
- Refactoring the code into functions or classes for cleaner structure and easier future expansion

## License

This project is provided for educational and personal use.

