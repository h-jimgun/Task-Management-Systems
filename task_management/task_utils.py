from datetime import datetime
from .validation import validate_due_date, validate_task_title, validate_task_description
# Import validation functions
# Define tasks list
tasks = [{}]
# Implement add_task function
def add_task(title, description, due_date):
    if not validate_task_title(title):
        print("Invalid task title.")
        return
    if not validate_task_description(description):
        print("Invalid task description.")
        return
    if not validate_due_date(due_date):
        print("Invalid due date.")
        return
    tasks.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    })
    print("Task added successfully!")
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    index = index - 1 
    if index < 0 or index >= len(tasks):
        print("Invalid task index.")
        return
    tasks[index]["completed"] = True
    print("Task marked as complete!")
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending_tasks = [task for task in tasks if not task["completed"]]
    if not pending_tasks:
        print("No pending tasks.")
    else:
        for i, task in enumerate(pending_tasks):
            print(f"{i}. {task['title']} - {task['description']} (Due: {task['due_date']})")
# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0
    completed_tasks = sum(1 for task in tasks if task["completed"])
    progress = (completed_tasks / len(tasks)) * 100
    return progress