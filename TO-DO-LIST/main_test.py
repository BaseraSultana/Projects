"""Menu-driven to-do list application."""

import file_handler


daily_task = file_handler.load_tasks("daily_tasks.txt")
weekly_task = file_handler.load_tasks("weekly_tasks.txt")
monthly_task = file_handler.load_tasks("monthly_tasks.txt")
yearly_task = file_handler.load_tasks("yearly_tasks.txt")
deleted_task = []


def get_menu_choice(prompt, minimum, maximum):
    """Prompt until the user enters an integer within the given range."""
    while True:
        choice = input(prompt).strip()
        try:
            choice = int(choice)
        except ValueError:
            print(
                f"Invalid input. Please enter a number between {minimum} and {maximum}.")
            continue
        if minimum <= choice <= maximum:
            return choice
        print(
            f"Invalid input. Please enter a number between {minimum} and {maximum}.")


def show_menu():
    """Display the main menu and process one selection."""
    menu = (
        "1. ADD TASK",
        "2. VIEW TASK",
        "3. SAVE TASK",
        "4. COMPLETE TASK",
        "5. DELETE TASK",
        "6. COMPLETED TASK HISTORY",
        "7. UNDO LAST DELETE",
        "8. EXIT",
    )
    print("\nTO-DO LIST\n" + "\n".join(menu))
    get_choice()


def get_choice():
    """Handle the user's selection from the main menu."""
    choice = get_menu_choice("Enter Your Choice: ", 1, 8)
    actions = {
        1: add_task,
        2: view_task,
        3: save_task,
        4: complete_task,
        5: delete_task,
        6: completed_task_history,
        7: undo_last_delete,
    }
    if choice == 8:
        print("Exiting.....")
        raise SystemExit
    actions[choice]()


def task_choice():
    """Prompt for a non-empty task description."""
    while True:
        task = input("Enter Your Task: ").strip()
        if task:
            return task
        print("Task cannot be empty. Please enter a task.")


def add_task():
    """Add a task to the selected category."""
    menu = (
        "1. DAILY TASK",
        "2. WEEKLY TASK",
        "3. MONTHLY TASK",
        "4. YEARLY TASK",
        "5. BACK TO MAIN MENU",
    )
    print("\nSelect the type of task you want to add:\n" + "\n".join(menu))
    choice = get_menu_choice("Enter Your Choice: ", 1, 5)
    if choice == 5:
        return

    task_lists = {
        1: daily_task,
        2: weekly_task,
        3: monthly_task,
        4: yearly_task,
    }
    task_lists[choice].append(task_choice())
    print("Task added successfully!")


def display_task_list(task_list, label):
    """Display the selected tasks or a relevant empty-state message."""
    if not task_list:
        print(f"No {label.lower()} available")
        return
    print(f"\n{label}:")
    for i, task in enumerate(task_list, start=1):
        print(f" {i}. {task}")


def view_task():
    """Display tasks for the selected category or all categories."""
    menu = (
        "1. DAILY TASKS",
        "2. WEEKLY TASKS",
        "3. MONTHLY TASKS",
        "4. YEARLY TASKS",
        "5. ALL TASKS",
        "6. BACK TO MAIN MENU",
    )
    print("\nSelect the type of task you want to view:\n" + "\n".join(menu))
    choice = get_menu_choice("Enter Your Choice: ", 1, 6)
    task_groups = {
        1: (daily_task, "Daily Tasks"),
        2: (weekly_task, "Weekly Tasks"),
        3: (monthly_task, "Monthly Tasks"),
        4: (yearly_task, "Yearly Tasks"),
        5: (daily_task + weekly_task + monthly_task + yearly_task, "All Tasks"),
    }
    if choice != 6:
        task_list, label = task_groups[choice]
        display_task_list(task_list, label)


def save_task():
    """Save the selected category or all tasks to their files."""
    menu = (
        "1. SAVE DAILY TASKS",
        "2. SAVE WEEKLY TASKS",
        "3. SAVE MONTHLY TASKS",
        "4. SAVE YEARLY TASKS",
        "5. SAVE ALL TASKS",
        "6. BACK TO MAIN MENU",
    )
    print("\nEnter the type of task you want to save:\n" + "\n".join(menu))
    choice = get_menu_choice("Enter Your Choice: ", 1, 6)
    save_groups = {
        1: (daily_task, "daily_tasks.txt"),
        2: (weekly_task, "weekly_tasks.txt"),
        3: (monthly_task, "monthly_tasks.txt"),
        4: (yearly_task, "yearly_tasks.txt"),
    }
    if choice == 6:
        return
    if choice == 5:
        for task_list, filename in (
            (daily_task, "daily_tasks.txt"),
            (weekly_task, "weekly_tasks.txt"),
            (monthly_task, "monthly_tasks.txt"),
            (yearly_task, "yearly_tasks.txt"),
        ):
            file_handler.save_tasks(task_list, filename)
        file_handler.save_tasks(
            daily_task + weekly_task + monthly_task + yearly_task,
            "all_tasks.txt",
        )
        print("All tasks saved successfully!")
        return

    task_list, filename = save_groups[choice]
    file_handler.save_tasks(task_list, filename)
    print(f"{filename} saved successfully!")


def complete_choice(task_list, filename):
    """Mark the selected task complete and persist the updated category."""
    if not task_list:
        print("No tasks available to complete.")
        return None
    display_task_list(task_list, "Tasks")
    index = get_menu_choice(
        "Enter which task you want to mark as complete: ", 1, len(task_list)
    ) - 1
    completed_task = task_list.pop(index)
    file_handler.save_tasks(task_list, filename)
    print(f"Task '{completed_task}' marked as complete.")
    return completed_task


def complete_task():
    """Mark a task complete in the selected category."""
    menu = (
        "1. DAILY TASK",
        "2. WEEKLY TASK",
        "3. MONTHLY TASK",
        "4. YEARLY TASK",
        "5. BACK TO MAIN MENU",
    )
    print("\nSelect the type of task you want to mark as complete:\n" + "\n".join(menu))
    choice = get_menu_choice("Enter Your Choice: ", 1, 5)
    task_groups = {
        1: (daily_task, "daily_tasks.txt"),
        2: (weekly_task, "weekly_tasks.txt"),
        3: (monthly_task, "monthly_tasks.txt"),
        4: (yearly_task, "yearly_tasks.txt"),
    }
    if choice == 5:
        return

    task_list, filename = task_groups[choice]
    completed = complete_choice(task_list, filename)
    if completed is not None:
        file_handler.append_completed_task(completed, "completed_tasks.txt")


def delete_choice(task_list, filename):
    """Delete a task from a category and persist the updated list."""
    if not task_list:
        print("No tasks available to delete.")
        return None
    display_task_list(task_list, "Tasks")
    index = get_menu_choice(
        "Enter which task you want to delete: ", 1, len(task_list)
    ) - 1
    removed_task = task_list.pop(index)
    file_handler.save_tasks(task_list, filename)
    print(f"Task '{removed_task}' is deleted.")
    return task_list, filename, index, removed_task


def delete_task():
    """Delete a task from the selected category."""
    menu = (
        "1. DAILY TASK",
        "2. WEEKLY TASK",
        "3. MONTHLY TASK",
        "4. YEARLY TASK",
        "5. BACK TO MAIN MENU",
    )
    print("\nSelect the type of task you want to delete:\n" + "\n".join(menu))
    choice = get_menu_choice("Enter Your Choice: ", 1, 5)
    task_groups = {
        1: (daily_task, "daily_tasks.txt"),
        2: (weekly_task, "weekly_tasks.txt"),
        3: (monthly_task, "monthly_tasks.txt"),
        4: (yearly_task, "yearly_tasks.txt"),
    }
    if choice == 5:
        return

    task_list, filename = task_groups[choice]
    deletion = delete_choice(task_list, filename)
    if deletion is not None:
        deleted_task.append(deletion)


def completed_task_history():
    """Display the history of completed tasks."""
    completed_tasks = file_handler.load_tasks("completed_tasks.txt")
    if not completed_tasks:
        print("No completed tasks available.")
        return
    print("\nCompleted Tasks History:")
    for i, task in enumerate(completed_tasks, start=1):
        print(f"{i}. {task}")


def undo_last_delete():
    """Restore the most recently deleted task if available."""
    if not deleted_task:
        print("No deleted tasks to undo.")
        return
    choice = get_menu_choice(
        "Do you want to undo the last delete?\n1. Yes\n2. No\nEnter Your Choice: ",
        1,
        2,
    )
    if choice == 1:
        task_list, filename, index, task = deleted_task.pop()
        task_list.insert(index, task)
        file_handler.save_tasks(task_list, filename)
        print(f"Restored task: {task}")


while True:
    show_menu()
