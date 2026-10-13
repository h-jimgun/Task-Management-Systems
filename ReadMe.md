# Task Management System

It's a system that checks for input validation on each task the user is prompted to input their values.

## Project Structure
The system contains the following components:

- `main.py`: The entry point where the user interacts with the task management system.
- `task_management/`: A package folder containing the core logic:
  - `task_utils.py`: Handles task utilities (adding, viewing, marking complete, calculating progress).
  - `__init__.py`: Initializes the Python package.
  - `validation.py`: Handles input validation for the tasks.

## How to Run
1. Open your terminal in the project root directory.
2. Run the following command:
   ```bash
   python3 main.py