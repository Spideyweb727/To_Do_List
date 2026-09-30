# To-Do List Manager

A simple Python based To-Do List application for managing daily tasks.

Users can add tasks, view their task list, mark tasks as completed, and delete tasks through a simple menu based interface.

This project was built to practice core Python programming concepts through a practical application.

## Features

* Add new tasks
* View all tasks
* Mark tasks as completed
* Delete tasks
* Validate task numbers
* Handle empty task lists
* Handle empty task input
* Simple menu based interface
* Windows `.exe` version available

## Example

```text
================= TO-DO LIST MANAGER =================

1. View Tasks
2. Add Task
3. Mark Task as Complete
4. Delete Task
5. Exit

=======================================================

Enter your choice:
```

Example task list:

```text
Sr. No.   Task                     Status
1         Learn Python             Pending
2         Build Company Analyzer   Done
3         Update GitHub            Pending
```

## Python Concepts Practiced

This project helped me practice:

* Variables
* User input
* Conditional statements
* `if`, `elif`, and `else`
* `while` loops
* `for` loops
* Lists
* Tuples
* List indexing
* `append()`
* `pop()`
* `len()`
* Boolean conditions
* Input validation
* String formatting
* Formatted output
* `break`
* Basic error handling

## How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/To-do-list.git
```

Move into the project directory:

```bash
cd To-do-list
```

Run the Python program:

```bash
python To_do_list.py
```

## Windows Executable

A Windows executable can be created using PyInstaller.

Install PyInstaller:

```bash
python -m pip install pyinstaller
```

Create the executable:

```bash
python -m PyInstaller --onefile --name ToDoListManager To_do_list.py
```

The executable will be created in:

```text
dist/ToDoListManager.exe
```

The `.exe` can be run without opening the Python source file.

## Project Structure

```text
To-do-list/
│
├── To_do_list.py
├── README.md
└── dist/
    └── ToDoListManager.exe
```

## Future Improvements

Potential improvements include:

* Add task priority
* Add due dates
* Add task categories
* Save tasks to a file
* Load tasks when the application starts
* Add search functionality
* Add sorting by status or priority
* Add a graphical user interface

## Disclaimer

This project is created for learning and educational purposes.

## Author

**Kalpesh Baviskar**

Market Research & Technology Analyst

Currently expanding my skills in Python, data analysis, automation, and financial data analysis.
