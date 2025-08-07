import json
from tasks import Task

TASKS_FILE = 'tasks.json'

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks_data = json.load(file)
            return [Task.from_dict(task) for task in tasks_data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON from tasks file.")
        return []

def save_tasks(tasks):
    tasks_data = [task.to_dict() for task in tasks]
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks_data, file, indent=4)

