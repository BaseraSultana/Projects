import file_handler


def show_menu():
    """Display the main menu and handle the user's selection."""
    menu = ("1. ADD TASK", "2. VIEW TASK", "3. SAVE TASK",
            "4. COMPLETE TASK", "5. DELETE TASK", "6. EXIT")
    print("\nTO-DO LIST\n" + "\n".join(menu))
    get_choice()


def get_choice():
    """Handle the user's selection from the main menu."""
    choice = int(input("Enter Your Choice: ").strip())
    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        save_task()
    elif choice == 4:
        complete_task()
    elif choice == 5:
        delete_task()
    elif choice == 6:
        print("Exiting.....")
        raise SystemExit
    else:
        print("Invalid Input. Try Again!")


daily_task = []
weekly_task = []
monthly_task = []
yearly_task = []


def task_choice():
    """Prompt the user for a task description and return it."""
    task = input("Enter Your Task: ")
    return task


def add_task():
    """Add a task to the selected task list."""
    menu = ("1. DAILY TASK", "2. WEEKLY TASK",
            "3. MONTHLY TASK", "4. YEARLY TASK", "5. EXIT")
    print("\nSelect the type of Task you want to add: \n" + "\n".join(menu))
    choice = int(input("Enter Your Choice: ").strip())
    if choice == 1:
        task = task_choice()
        daily_task.append(task)
    elif choice == 2:
        task = task_choice()
        weekly_task.append(task)
    elif choice == 3:
        task = task_choice()
        monthly_task.append(task)
    elif choice == 4:
        task = task_choice()
        yearly_task.append(task)
    elif choice == 5:
        print("Exiting.....")
        show_menu()
    else:
        print("Invalid Input. Try Again!")
        add_task()


def display_task_list(task_list, label):
    """Display the selected tasks or a relevant empty-state message."""
    if not task_list:
        print(f"No {label.lower()} available")
        return

    print(f"\n {label}: ")
    for task in task_list:
        print(task)


def view_task():
    """Display tasks for the selected category or all tasks."""
    menu = ("1. DAILY TASKS", "2. WEEKLY TASKS", "3. MONTHLY TASKS",
            "4. YEARLY TASKS", "5. ALL TASKS", "6. EXIT")
    print("\nSelect the type of Task you want to view: \n" + "\n".join(menu))
    choice = int(input("Enter Your Choice:").strip())

    if choice == 6:
        print("Exiting.....")
        show_menu()
        return

    task_groups = {
        1: (daily_task, "Daily Tasks"),
        2: (weekly_task, "Weekly Tasks"),
        3: (monthly_task, "Monthly Tasks"),
        4: (yearly_task, "Yearly Tasks"),
        5: (daily_task + weekly_task + monthly_task + yearly_task, "All Tasks"),
    }

    if choice not in task_groups:
        print("Invalid Input. Try Again!")
        show_menu()
        return

    task_list, label = task_groups[choice]
    display_task_list(task_list, label)


def save_task():
    """Save the selected task list to storage or return to the main menu."""
    menu = ("1. SAVE DAILY TASKS", "2. SAVE WEEKLY TASKS", "3.SAVE MONTHLY TASKS",
            "4. SAVE YEARLY TASKS", "5. SAVE ALL TASKS", "6. EXIT")
    print("Enter the type of task you want to save: \n" + "\n".join(menu))
    choice = int(input("Enter Your Choice: ").strip())
    if choice == 1:
        file_handler.save_daily()
    elif choice == 2:
        file_handler.save_weekly()
    elif choice == 3:
        file_handler.save_monthly()
    elif choice == 4:
        file_handler.save_yearly()
    elif choice == 5:
        file_handler.save_all()
    elif choice == 6:
        print("Exiting.....")
        show_menu()
    else:
        print("Invalid Input. Try Again!")
        save_task()
