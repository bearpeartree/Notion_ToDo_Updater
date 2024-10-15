from .Task import Task
import datetime

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