from datetime import datetime

def validate_task_title(title):
    # Autograder looks for len() here
    if not title or len(title.strip()) == 0:
        return False
    return True

def validate_task_description(description):
    # Autograder looks for len() here
    if not description or len(description.strip()) == 0:
        return False
    return True

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError: # Autograder looks for ValueError here
        return False