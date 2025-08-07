from datetime import datetime

class Task:
    def __init__(self, title, description, deadline, completed=False):
        self.title = title
        self.description = description
        self.deadline = datetime.strptime(deadline, '%Y-%m-%d %H:%M')
        self.completed = completed

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline.strftime('%Y-%m-%d %H:%M'),
            "completed": self.completed
        }
    
    @staticmethod
    def from_dict(data):
        return Task(
            title=data['title'],
            description=data['description'],
            deadline=data['deadline'],
            completed=data.get('completed', False)
        )