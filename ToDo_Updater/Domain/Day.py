from .Task import Task

class Day:
    def __init__(self, date_time):
        self.date_time = date_time
        self.tasks = []

    def get_date(self):
        return self.date_time
    
    def get_tasks(self):
        return self.tasks
    
    def add_task(self, task):
        if task != "":
            self.tasks.append(task)
        else:
            raise ValueError("Der Name der Aufgabe darf nicht leer sein!")