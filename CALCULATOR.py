"""Simple calculator application."""


def get_numbers():
    """Read two integer values from the user."""
    one = int(input("Enter the First number: ").strip())
    two = int(input("Enter the Second number: ").strip())
    return one, two


def display_result(result):
    """Display a calculation result and ask whether to continue."""
    print(f"Result = {result:.2f}")
    history()
    print("Do You Want To Continue?\n", "1. Yes\n", "2. No\n")
    choice = int(input("Enter Your Choice: ").strip())
    if choice == 1:
        show_menu()
    elif choice == 2:
        print("Exiting.....")
        raise SystemExit
    else:
        print("Invalid Input")


def add():
    """Add two numbers."""
    one, two = get_numbers()
    result = one + two
    display_result(result)


def subtract():
    """Subtract the second number from the first."""
    one, two = get_numbers()
    result = one - two
    display_result(result)


def multiply():
    """Multiply two numbers."""
    one, two = get_numbers()
    result = one * two
    display_result(result)


def divide():
    """Divide the first number by the second."""
    one, two = get_numbers()
    if two == 0:
        print("Not defined")
    else:
        result = one / two
        display_result(result)


def modulus():
    """Find the remainder when the first number is divided by the second."""
    one, two = get_numbers()
    if two == 0:
        print("Not defined")
    else:
        result = one % two
        display_result(result)


def exponent():
    """Raise the first number to the power of the second."""
    one, two = get_numbers()
    if one == 0 and two == 0:
        print("Not defined")
    else:
        result = one ** two
        display_result(result)


def floor_division():
    """Return the integer quotient of the two numbers."""
    one, two = get_numbers()
    if two == 0:
        print("Not defined")
    else:
        result = one // two
        print(f"Result = {result}")
        print("Do You Want To Continue?\n", "1. Yes\n", "2. No\n")
        choice = int(input("Enter Your Choice: ").strip())
        if choice == 1:
            show_menu()
        elif choice == 2:
            print("Exiting.....")
            raise SystemExit
        else:
            print("Invalid Input")


def history():
    """Display the calculation history."""
    history_entries = []
    history_entries.append(result)


def calculation_history():
    history_entries = history()
    if len(history_entries) == 0:
        print("No calculation history available")
    else:
    for i in history:
        print(i)


def get_choice():
    """Handle the user's menu selection."""
    choice = int(input("Enter Your Choice: ").strip())
    if choice == 1:
        add()
    elif choice == 2:
        subtract()
    elif choice == 3:
        multiply()
    elif choice == 4:
        divide()
    elif choice == 5:
        modulus()
    elif choice == 6:
        exponent()
    elif choice == 7:
        floor_division()
    elif choice == 8:

    elif choice == 9:
        print("Exiting....")
        raise SystemExit
    else:
        print("Invalid Input. Try Again!")


def show_menu():
    """Display the calculator menu and process a selection."""
    menu = ("1. ADDITION", "2. SUBTRACTION",
            "3. MULTIPLICATION", "4. DIVISION", "5. MODULUS", "6. EXPONENT", "7. FLOOR DIVISION", "8. HISTORY", "9. EXIT")
    print("\nCALCULATOR MENU\n" + "\n".join(menu))
    get_choice()


while True:
    show_menu()
