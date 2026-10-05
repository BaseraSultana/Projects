import main


def save_daily():
    """Save the daily tasks to the todo list file."""
    with open("list.txt", "w", encoding="utf-8") as file:
        for task in main.daily_task:
            file.write(task + "\n")


def save_weekly():
    """Save the weekly tasks to the todo list file."""
    with open("list.txt", "w", encoding="utf-8") as file:
        for task in main.weekly_task:
            file.write(task + "\n")


def save_monthly():
    """Save the monthly tasks to the todo list file."""
    with open("list.txt", "w", encoding="utf-8") as file:
        for task in main.monthly_task:
            file.write(task + "\n")


def save_yearly():
    """Save the yearly tasks to the todo list file."""
    with open("list.txt", "w", encoding="utf-8") as file:
        for task in main.yearly_task:
            file.write(task + "\n")


def save_all():
    """Save all tasks to the todo list file."""
    with open("list.txt", "w", encoding="utf-8") as file:
        for task in main.daily_task + main.weekly_task + main.monthly_task + main.yearly_task:
            file.write(task + "\n")


def load_tasks():
    """Load tasks from the todo list file into the respective task lists."""
    try:
        with open("list.txt", "r", encoding="utf-8") as file:
            for line in file:
                task = line.strip()
                if task.startswith("Daily:"):
                    main.daily_task.append(task)
                elif task.startswith("Weekly:"):
                    main.weekly_task.append(task)
                elif task.startswith("Monthly:"):
                    main.monthly_task.append(task)
                elif task.startswith("Yearly:"):
                    main.yearly_task.append(task)
    except FileNotFoundError:
        print("No saved tasks found. Starting with empty task lists.")
