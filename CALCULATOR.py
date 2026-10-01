"""Simple calculator application."""


def get_numbers():
    """Read two integer values from the user."""
    one = int(input("Enter the First number: ").strip())
    two = int(input("Enter the Second number: ").strip())
    return one, two


def display_result(result):
    """Display a calculation result and ask whether to continue."""
    print(f"Result = {result:.2f}")
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
        print("Exiting....")
        raise SystemExit
    else:
        print("Invalid Input. Try Again!")


def show_menu():
    """Display the calculator menu and process a selection."""
    menu = ("1. ADDITION", "2. SUBTRACTION",
            "3. MULTIPLICATION", "4. DIVISION", "5. EXIT")
    print("\nCALCULATOR MENU\n" + "\n".join(menu))
    get_choice()


while True:
    show_menu()
