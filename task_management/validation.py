from datetime import datetime
def validate_task_title(title):
    if not title or not title.strip():
        return False
    return True


def validate_task_description(description):
    if not description or not description.strip():
        return False
    return True
def validate_due_date(due_date):
    try:
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        if due_date_obj.date() < datetime.today().date():
            return False
        return True
    except ValueError:
        return False