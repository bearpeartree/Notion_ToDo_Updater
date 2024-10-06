from datetime import date
from . import Task

class Day:
    def __init__(self, day, in_week_cal):
        self.day = day
        self.in_week_cal = in_week_cal
        self.tasks = []

    def get_day(self):
        return self.day
    
    def get_in_week_cal(self):
        return self.get_in_week_cal
    
    def get_tasks(self):
        return self.tasks
    
    def add_task(self, task):
        self.tasks.append(task)