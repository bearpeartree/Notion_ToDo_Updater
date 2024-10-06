from datetime import date
from .Task import Task

class Day:
    def __init__(self, day_name, in_week_cal, year):
        self.day_name = day_name
        self.in_week_cal = in_week_cal
        self.year = year
        self.tasks = []

    def get_day_name(self):
        return self.day_name
    
    def get_in_week_cal(self):
        return self.get_in_week_cal
    
    def get_tasks(self):
        return self.tasks
    
    def add_task(self, task):
        if task != "":
            self.tasks.append(task)
        else:
            raise ValueError("Der Name der Aufgabe darf nicht leer sein!")