def show_menu():
    menu = ("1. ADD TASK", "2. VIEW TASK",
            "3. COMPLETE TASK", "4. DELETE TASK", "5. EXIT")
    print("\nTO-DO LIST\n" + "\n".join(menu))
    get_choice()


def get_choice():
    choice = int(input("Enter Your Choice: ").strip())
    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        complete_task()
    elif choice == 4:
        delete_task()
    elif choice == 5:
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


def add_task(task):
    """Add a task to the selected task list."""
    menu = ("1. DAILY TASK", "2. WEEKLY TASK",
            "3. MONTHLY TASK", "4. YEARLY TASK")
    print("\nSelect the type of Task you want to add: \n" + "\n".join(menu))
    choice = int(input("Enter Your Choice: ").strip())
    if choice == 1:
        task_choice()
        daily_task.append(task)
