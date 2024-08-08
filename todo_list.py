import os
import csv


def clear_terminal():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Unix (Linux, macOS)
    else:
        os.system('clear')

# Clase que representa una tarea en la lista
class TaskItem:
    def __init__(self, description, status="Pending"):
        self.description = description
        self.status = status

    def mark_complete(self):
        self.status = "Completed"
    
    def mark_in_progress(self):
        self.status = "In Progress"

    def __str__(self):
        return f"{self.description} [{self.status}]"

# Clase que gestiona la colección de tareas
class TaskListManager:
    def __init__(self, storage_file="task_list.csv"):
        self.tasks = []
        self.storage_file = storage_file
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, mode='r') as file:
                reader = csv.reader(file)
                self.tasks = [TaskItem(description, status) for description, status in reader]

    def save_tasks(self):
        with open(self.storage_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for task in self.tasks:
                writer.writerow([task.description, task.status])

    def add_task(self, description):
        new_task = TaskItem(description)
        self.tasks.append(new_task)
        self.save_tasks()

    def list_tasks(self):
        return self.tasks

    def mark_task_complete(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_complete()
                self.save_tasks()
                return
        raise ValueError("Task not found")
    
    def mark_task_in_progress(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_in_progress()
                self.save_tasks()
                return
        raise ValueError("Task not found")
