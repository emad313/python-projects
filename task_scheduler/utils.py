def print_task(task, index=None):
    status = "Pending" if not task.is_completed else "Completed"
    index_str = f"{index + 1}. " if index is not None else ""
    print(f"{index_str}{status} - {task.title} (Deadline: {task.deadline.strftime('%Y-%m-%d %H:%M')})")