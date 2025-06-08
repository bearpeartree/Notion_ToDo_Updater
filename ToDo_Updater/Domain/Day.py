from .Task import Task
from .Exceptions.TaskNotFoundError import TaskNotFoundError
from datetime import datetime

class Day:
    def __init__(self, date_time):
        self.date_time = date_time
        self.tasks = []

    def get_date(self):
        return self.date_time
    
    def get_tasks(self):
        return self.tasks


    def get_all_tasks_names(self):
        tasks_names = []
        for t in self.tasks:
            tasks_names.append(t.get_task_name())
        
        return tasks_names
    

    def add_task(self, task):
        if task != "":
            self.tasks.append(Task(task, self.date_time))
        else:
            raise ValueError("Der Name der Aufgabe darf nicht leer sein!")
    
    # returns the week calendar the date is falling under
    def get_week_calendar(self):
        return self.date_time.isocalendar()[1]
    

    def get_week_day(self):
        number_week_day = self.date_time.isoweekday()
        match number_week_day:
            case 1:
                return "montag"
            case 2:
                return "dienstag"
            case 3:
                return "mittwoch"
            case 4:
                return "donnerstag"
            case 5:
                return "freitag"
            case 6:
                return "samstag"
            case 7:
                return "sonntag"
            
    
    def get_unfinished_tasks(self):
        unfinished = []
        for t in self.tasks:
            if t.is_finished() == False:
                unfinished.append(t)
        
        return unfinished
    

    def add_task_list_to_task(self, tasks):
        return self.tasks.extend(tasks)
    

    def format_datetime_to_string(self):
        year = self.date_time.strftime("%Y")
        month = self.date_time.strftime("%m")
        day = self.date_time.strftime("%d")
        return day + "." + month + "." + year
    

    def find_correct_task(self, task_name):
        for t in self.tasks:
            if t.get_task_name() == task_name:
                return t
        raise TaskNotFoundError("Die TODO konnte nicht gefunden werden.")
    