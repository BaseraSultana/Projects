import file_handler


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


def view_task():
    menu = ("1. DAILY TASKS", "2.WEEKLY TASKS,"3. MONTHLY TASKS","4. YEARLY TASKS","5. ALL TASKS","6.EXIT")
      print("\nSelect the type of Task you want to view: \n" + "\n".join(menu))
      choice = int(input("Enter Your Choice:").strip())
      if choice == 1:
        if len(daily_task) == 0:
            print("No daily tasks available")
            view_task()
        else:
            print("\n Daily Tasks: ")
            for task in daily_task:
                print(task)
    elif choice == 2:
        if len(weekly_task) == 0:
            print("No daily tasks available")
            view_task()
        else:
            print("\n Weekly Tasks: ")
            for task in weekly_task:
                print(task)
    elif choice == 3:
        if len(monthly_task) == 0:
            print("No daily tasks available")
            view_task()
        else:
            print("\n Monthly Tasks: ")
            for task in monthly_task:
                print(task)
    elif choice == 4:
        if len(yearly_task) == 0:
            print("No daily tasks available")
            view_task()
        else:
            print("\n Yearly Tasks: ")
            for task in yearly_task:
                print(task)
    elif choice == 5:
        if len(daily_task + weekly_task + monthly_task + yearly_task) == 0:
            print("No daily tasks available")
            view_task()
        else:
            print("\n All Tasks: ")
            for task in daily_task + weekly_task + monthly_task + yearly_task:
                print(task)
    elif choice == 6:
        print("Exiting.....")
        show_menu()
    else:
        print("Invalid Input. Try Again!")
        show_menu()

def save_task():
    menu = ("1. SAVE DAILY TASKS", "2. SAVE WEEKLY TASKS", "3.SAVE MONTHLY TASKS","4. SAVE YEARLY TASKS", "5. SAVE ALL TASKS","6. EXIT")  
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
    elif choice== 6:
        print("Exiting.....")
        show_menu()
    else:
        print("Invalid Input. Try Again!")
        save_task()
        