# To-Do List

A menu-driven command-line task manager written in Python. Organize tasks by how often they need attention, keep them in text files, and track completed tasks.

## Technologies Used

- Python 3
- Python standard library (`pathlib`)
- Command-line interface
- Plain-text files for task storage

## Skills Practiced

This project practices using functions, loops, conditionals, user input, lists, dictionaries, file handling, and basic input validation.

## Author

**Basera Sultana**

## Features

- Add tasks to daily, weekly, monthly, or yearly categories
- View tasks by category or view all tasks
- Save a category or save all categories to text files
- Mark tasks as complete and view completed-task history
- Delete tasks and undo the most recent deletion during the current run
- Load saved category tasks when the program starts

## Requirements

- Python 3.x
- No third-party packages required

## How to Run

Open a terminal in the project folder and run:

```bash
python main.py
```

On Windows, you can also run:

```powershell
py main.py
```

## How to Use

Choose an option from the main menu by entering its number:

1. Add a task and choose its frequency category.
2. View tasks for a category or view all tasks.
3. Save tasks for a category or save all tasks.
4. Mark a task as complete by choosing its category and task number.
5. Delete a task by choosing its category and task number.
6. View completed-task history.
7. Restore the most recently deleted task from the current run.
8. Exit.

## Task Storage

Tasks are stored in text files in the project folder:

- `daily_tasks.txt`
- `weekly_tasks.txt`
- `monthly_tasks.txt`
- `yearly_tasks.txt`
- `all_tasks.txt` (written when you choose to save all tasks)
- `completed_tasks.txt` (records tasks marked complete)

Newly added tasks remain in memory until you save them. Save your tasks before exiting if you want to keep them. Marking a task complete or deleting one updates its category file immediately. The undo-delete feature is available only during the current program run.

## Example

```text
TO-DO LIST
1. ADD TASK
2. VIEW TASK
3. SAVE TASK
4. COMPLETE TASK
5. DELETE TASK
6. COMPLETED TASK HISTORY
7. UNDO LAST DELETE
8. EXIT

Enter Your Choice: 1
Select the type of Task you want to add:
1. DAILY TASK
2. WEEKLY TASK
3. MONTHLY TASK
4. YEARLY TASK
5. EXIT
Enter Your Choice: 1
Enter Your Task: Review Python notes
Task added successfully!
```

## Future Improvements

- Save new tasks automatically so they are not lost when exiting
- Add due dates, priorities, or reminders
- Allow editing existing tasks
- Add a search or filter option
- Make undo available across program restarts
- Add automated tests for task operations and file storage
- Improve menu navigation and input validation

## Project Structure

```text
TO-DO-LIST/
├── main.py
├── file_handler.py
├── daily_tasks.txt
├── weekly_tasks.txt
├── monthly_tasks.txt
├── yearly_tasks.txt
├── all_tasks.txt
├── completed_tasks.txt
└── README.md
```