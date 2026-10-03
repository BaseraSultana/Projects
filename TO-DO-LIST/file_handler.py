try:
    import main
except IndentationError as exc:
    raise ImportError(
        "Cannot import main because main.py has an indentation error "
        "(expected an indented block after the function definition on line 63)."
    ) from exc


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
