while True:

    def get_numbers():
        one = int(input("Enter the First number: ").strip())
        two = int(input("Enter the Second number: ").strip())

    def display_result():
        print(f"Result = {result}")
        print("Do You Want To Continue?\n", "1. Yes\n", "2. No\n")
        choice = int(input("Enter Your Choice: ").strip())
        if choice == "1":
            continue
        elif choice == "2":
            print("Exiting.....")
            break
        else:
            print("Invalid Input")

    def add():
        get_numbers()
        result = one + two
        display_result()

    def subtra

    def show_menu():
        menu = ("1. ADDITION", "2. SUBTRACTION",
                "3. MULTIPLICATION", "4. DIVISION", "5. EXIT")
        print("\nCALCULATOR MENU\n" + "\n".join(menu))
        get_choice()

    def get_choice():
        choice = int(input("Enter Your Choice: ").strip())
        if choice == "1":
            def add()
        elif choice == "2":
            def subtract()
        elif choice == "3":
            def multiply()
        elif choice == "4":
            def divide()
        elif choice == "5":
            print("Exiting....")
            break
        else:
            print("Invalid Input. Try Again!")
