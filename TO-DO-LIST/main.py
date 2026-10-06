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
        undo_last_delete()
    elif choice == 7:
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
    i = 1
    print(f"\n {label}: ")
    for task in task_list:
        print(f"{i}. {task}")
        i += 1


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
    if choice == 5:
        display_task_list(daily_task, "Daily Tasks")
        display_task_list(weekly_task, "Weekly Tasks")
        display_task_list(monthly_task, "Monthly Tasks")
        display_task_list(yearly_task, "Yearly Tasks")

    if choice not in task_groups:
        print("Invalid Input. Try Again!")
        show_menu()
        return

    else:
        task_list, label = task_groups[choice]
        display_task_list(task_list, label)


def save_task():
    """Save the selected task list to storage or return to the main menu."""
    menu = ("1. SAVE DAILY TASKS", "2. SAVE WEEKLY TASKS", "3.SAVE MONTHLY TASKS",
            "4. SAVE YEARLY TASKS", "5. SAVE ALL TASKS", "6. EXIT")
    print("Enter the type of task you want to save: \n" + "\n".join(menu))
    choice = int(input("Enter Your Choice: ").strip())
    save_groups = {
        1: (daily_task, "daily_tasks.txt"),
        2: (weekly_task, "weekly_tasks.txt"),
        3: (monthly_task, "monthly_tasks.txt"),
        4: (yearly_task, "yearly_tasks.txt"),
        5: (daily_task + weekly_task + monthly_task + yearly_task, "all_tasks.txt")
    }

    if choice == 6:
        print("Exiting.....")
        show_menu()
        return

    if choice in save_groups:
        task_list, label = save_groups[choice]
        file_handler.save_tasks(task_list, label)
        return

    print("Invalid Input. Try Again!")
    save_task()

    # if choice == 1:
    #     file_handler.save_daily()
    # elif choice == 2:
    #     file_handler.save_weekly()
    # elif choice == 3:
    #     file_handler.save_monthly()
    # elif choice == 4:
    #     file_handler.save_yearly()
    # elif choice == 5:
    #     file_handler.save_all()
    # elif choice == 6:
    #     print("Exiting.....")
    #     show_menu()
    # else:
    #     print("Invalid Input. Try Again!")
    #     save_task()


def complete_choice(type_of_task, filename):
    """Prompt the user to select a task to mark as complete."""
    choice = input("Enter which task you want to mark as complete: ")
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(type_of_task):
            completed_task = type_of_task.pop(index)
            print(f"Task '{completed_task}' marked as complete.")
            file_handler.save_tasks(type_of_task, filename)
            return completed_task
        else:
            print("Invalid task number. Please try again.")
    else:
        print("Invalid input. Please enter a valid number.")


def complete_task():
    """Mark a task as complete for the selected category."""
    menu = ("1. DAILY TASK", "2. WEEKLY TASK",
            "3. MONTHLY TASK", "4. YEARLY TASK", "5. EXIT")
    print("Select the type of task you want to mark as complete: \n" + "\n".join(menu))
    choice = int(input("Enter Your Choice: ").strip())
    task_groups = {
        1: (daily_task, "Daily Tasks", "daily_tasks.txt"),
        2: (weekly_task, "Weekly Tasks", "weekly_tasks.txt"),
        3: (monthly_task, "Monthly Tasks", "monthly_tasks.txt"),
        4: (yearly_task, "Yearly Tasks", "yearly_tasks.txt"),
    }

    if choice in task_groups:
        task_list, label, filename = task_groups[choice]
        display_task_list(task_list, label)
        completed_task = complete_choice(task_list, filename)
        if completed_task is not None:
            file_handler.append_completed_task(
                completed_task, "completed_tasks.txt")
    elif choice == 5:
        print("Exiting.....")
        show_menu()
        return
    else:
        print("Invalid Input. Try Again!")
        complete_task()


def delete_choice(type_of_task, filename):
    """Delete a task from a task list and persist the updated list."""
    choice = input("Enter which task you want to delete: ")
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(type_of_task):
            removed_task = type_of_task.pop(index)
            print(f"Task '{removed_task}' is deleted.....")
            file_handler.save_tasks(type_of_task, filename)
            return removed_task
        print("Invalid task number. Please try again.")
        return None
    print("Invalid input. Please enter a valid number.")
    return None


deleted_task = []


def delete_task():
    """Delete a task from the selected category."""
    menu = ("1. DAILY TASK", "2. WEEKLY TASK",
            "3. MONTHLY TASK", "4. YEARLY TASK", "5. EXIT")
    print("Select the type of task you want to delete: \n" + "\n".join(menu))
    choice = int(input("Enter Your Choice: ").strip())
    task_groups = {
        1: (daily_task, "Daily Tasks", "daily_tasks.txt"),
        2: (weekly_task, "Weekly Tasks", "weekly_tasks.txt"),
        3: (monthly_task, "Monthly Tasks", "monthly_tasks.txt"),
        4: (yearly_task, "Yearly Tasks", "yearly_tasks.txt"),
    }

    if choice in task_groups:
        task_list, label, filename = task_groups[choice]
        display_task_list(task_list, label)
        removed_task = delete_choice(task_list, filename)
        if removed_task is not None:
            deleted_task.append(removed_task)
    elif choice == 5:
        print("Exiting.....")
        show_menu()
        return
    else:
        print("Invalid Input. Try Again!")
        delete_task()


def undo_last_delete():
    print("Do you want to undo last delete?\n", "1. Yes\n", "2. No")
    choice = int(input("Enter Your Choice: ").strip())
    if choice == 1:
