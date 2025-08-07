from tasks import Task
from storage import load_tasks, save_tasks
from utils import print_task

def main():
    tasks = load_tasks()

    while True:
        print("\nTask Scheduler")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            if not tasks:
                print("No tasks available.")
            else:
                for index, task in enumerate(tasks):
                    print_task(task, index)
        elif choice == '2':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            deadline = input("Enter task deadline (YYYY-MM-DD HH:MM): ")
            try:
                new_task = Task(title, description, deadline)
                tasks.append(new_task)
                save_tasks(tasks)
                print("Task added successfully.")
            except ValueError as e:
                print(f"Error adding task: {e}")
        elif choice == '3':
            if not tasks:
                print("No tasks available to mark as completed.")
            else:
                for index, task in enumerate(tasks):
                    print_task(task, index)
                    task_input = input("Enter the task number to mark as completed: ")
                    if task_input.isdigit():
                        task_index = int(task_input) - 1
                        if 0 <= task_index < len(tasks):
                            tasks[task_index].completed = True
                            save_tasks(tasks)
                            print("Task marked as completed.")
                        else:
                            print("Invalid task number.")
                    else:
                        print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting Task Scheduler.")
            break
if __name__ == "__main__":
    main()