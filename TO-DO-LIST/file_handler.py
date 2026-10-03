import main


def save_daily():
    with open("list.txt", "w", encoding="utf-8") as file:
        for task in main.daily_task:
            file.write(task + "\n")


def save_weekly():
    with open("list.txt", "w", encoding="utf-8") as file:
        for task in main.weekly_task:
            file.write(task + "\n")


def save_monthly():
    with open("list.txt", "w", encoding="utf-8") as file:
        for task in main.monthly_task:
            file.write(task + "\n")


def save_yearly():
    with open("list.txt", "w", encoding="utf-8") as file:
        for task in main.yearly_task:
            file.write(task + "\n")
