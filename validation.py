from datetime import datetime

def validate_task_title(title):
    if not title or len(title) == 0:
        return False
    return True

def validate_task_description(description):
    if not description or len(description) == 0:
        return False
    return True

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False