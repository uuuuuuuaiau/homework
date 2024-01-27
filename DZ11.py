class Task:
    def __init__(self, task_id, title, description, completed=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        return f"Task ID: {self.task_id}\nTitle: {self.title}\nDescription: {self.description}\nCompleted: {self.completed}"


class TaskManager:
    def __init__(self, database_manager):
        self.tasks = []
        self.database_manager = database_manager

    def add_task(self, title, description):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, title, description)
        self.tasks.append(new_task)
        self.database_manager.save_task(new_task)

    def complete_task(self, task_id):
        task = next((t for t in self.tasks if t.task_id == task_id), None)
        if task:
            task.completed = True
            self.database_manager.update_task(task)

    def show_tasks(self):
        for task in self.tasks:
            print(task)

class DatabaseManager:
    def __init__(self, database_url):
        self.database_url = database_url
        self.connection = None

    def connect(self):
        pass

    def run(self):
        pass

    def save_task(self, task):
        pass

    def update_task(self, task):
        pass


# main.py

if __name__ == "__main__":
    database_url = "example_database_url"
    database_manager = DatabaseManager(database_url)
    database_manager.connect()

    task_manager = TaskManager(database_manager)

    task_manager.add_task("Task 1", "Description for Task 1")
    task_manager.add_task("Task 2", "Description for Task 2")

    task_manager.show_tasks()

    task_manager.complete_task(1)

    task_manager.show_tasks()

    if database_manager.connection:
        database_manager.connection.close()