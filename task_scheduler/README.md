# 🗓️ Task Scheduler

A simple command-line Task Scheduler written in Python. This project lets you add, list, and delete tasks with deadlines using persistent storage (JSON-based).

## 📂 Project Structure

task_scheduler/  
├── scheduler.py        # Main CLI script  
├── tasks.py            # Task class and logic  
├── storage.py          # Task persistence (JSON)  
├── utils.py            # Helper functions (e.g., date formatting)  
└── requirements.txt    # Dependencies (if any)

## ✅ Features

- Add tasks with deadlines  
- List all scheduled tasks  
- Delete tasks by ID  
- Persistent storage using JSON file  
- CLI-based interaction

## 🚀 Getting Started

1. Clone the repo:  
   git clone https://github.com/yourusername/task_scheduler.git  
   cd task_scheduler

2. Install dependencies:  
   pip install -r requirements.txt  
   *(You might not need this if you're only using Python’s built-in modules.)*

3. Run the application:  
   python scheduler.py

## 💡 Usage Examples

- Add a task:  
  python scheduler.py add "Buy groceries" "2025-08-08 18:30"

- List all tasks:  
  python scheduler.py list

- Delete a task:  
  python scheduler.py delete <task_id>

## 📌 Date Format

All deadlines must follow this format:  
YYYY-MM-DD HH:MM  
Example: 2025-08-08 18:30

## 📦 Dependencies

- Python 3.6+  
- Built-in modules:  
  argparse, json, os, datetime, uuid


## Example

$ python scheduler.py add "Doctor appointment" "2025-08-12 10:30"
Task added successfully!

$ python scheduler.py list
+--------------------------------------+---------------------+----------------------+
| ID                                   | Title               | Deadline             |
+--------------------------------------+---------------------+----------------------+
| a12f3a9e-2432-4c91-b2f1-9a1ac3f45e62 | Doctor appointment  | 2025-08-12 10:30     |
+--------------------------------------+---------------------+----------------------+

$ python scheduler.py delete a12f3a9e-2432-4c91-b2f1-9a1ac3f45e62
Task deleted successfully.

## 📄 License

MIT License © 2025

---

Built with 💻 by Emad Uddin
