from datetime import datetime

def validate_task_title(title):
    if title is None:
        return False
    if len(title.strip()) == 0:
        return False
    return True

def validate_task_description(description):
    if description is None:
        return False
    if len(description.strip()) == 0:
        return False
    return True

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False