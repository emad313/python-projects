import time
from datetime import datetime

# Store Task in a simple list (Can replace with DB or file later)

tasks = []

def add_task():
    name = input("Enter task name: ")
    description = input("Enter task description:")
    time_str = input("Scheduled time (YYYY-MM-DD HH:MM): ")

    try:
        scheduled_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        tasks.append({
            'name': name,
            'description': description,
            "time": scheduled_time
        })
        print(f"Task '{name}' added for {scheduled_time}.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD HH:MM.")

def view_tasks():
    if not tasks:
        print("No Tasks scheduled.")
    for task in tasks:
        print(f"Task: {task['name']}, Description: {task['description']}, Scheduled Time: {task['time']}")
    
def delete_task():
    view_tasks()
    if not tasks:
        return
    idx = input("Enter the task number to delete: ")
    if idx.isdigit():
        idx = int(idx) - 1
        if 0 <= idx <  len(tasks):
            removed_task = tasks.pop(idx)
            print(f"Task '{removed_task['name']}' deleted.")
        else:
            print("Invalid task number.")
    else:
        print("Please enter a valid number.")

def check_tasks():
    now = datetime.now()
    for task in tasks[:]:
        if task["time"] <= now:
            print(f"Executing Task: {task['name']}, Description: {task['description']}")
            tasks.remove(task)
            print(f"Task '{task['name']}' completed and removed from the list.")

def run_scheduler():
    print("Task Scheduler is running... Press Ctrl+C to stop.")
    try:
        while True:
            check_tasks()
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nTask Scheduler stopped.")

def main():
    while True:
        print("\nTask Scheduler Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Run Scheduler")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            run_scheduler()
        elif choice == '5':
            print("Exiting Task Scheduler.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()