from .Day import Day
from .Exceptions import IllegalDay
from .day_factory import day_factory as df
import datetime

# WEEK IST AGGREGAT

class Week:
    def __init__(self, day, month, year):
        try:
            dienstag = df.create_day(year, month, day).date_time + datetime.timedelta(days=1)
            mittwoch = df.create_day(year, month, day).date_time + datetime.timedelta(days=2)
            donnerstag = df.create_day(year, month, day).date_time + datetime.timedelta(days=3)
            freitag = df.create_day(year, month, day).date_time + datetime.timedelta(days=4)
            samstag = df.create_day(year, month, day).date_time + datetime.timedelta(days=5)
            sonntag = df.create_day(year, month, day).date_time + datetime.timedelta(days=6)

            self.days = {"montag": df.create_day(year, month, day), # immer den Startday angeben von jeder Woche lol
                        "dienstag": df.create_day(dienstag.year, dienstag.month, dienstag.day),
                        "mittwoch": df.create_day(mittwoch.year, mittwoch.month, mittwoch.day),
                        "donnerstag": df.create_day(donnerstag.year, donnerstag.month, donnerstag.day),
                        "freitag": df.create_day(freitag.year, freitag.month, freitag.day),
                        "samstag": df.create_day(samstag.year, samstag.month, samstag.day),
                        "sonntag": df.create_day(sonntag.year, sonntag.month, sonntag.day) 
                        }
            self.month = month
            self.year = year
        except(ValueError) as e:
            print("Datum ungültig")
            raise e


    def get_week_calendar(self):
        first_weekday = self.days["montag"]
        return first_weekday.date_time.isocalendar()[1]
    

    def get_day(self, day_name):
        day_name = day_name.lower()
        if day_name not in self.days:
            raise IllegalDay.IllegalDayException("Der Tag existiert nicht!")
        else:
            return self.days[day_name]
        

    def get_month(self):
        return self.month
    

    def get_days(self):
        return self.days
    

    # ToDo zu einem Tag hinzufügen
    # Später in service - Kalenderwoche + Wochentag als String
    def add_todo_to_day(self, day_name, task_name):
        current_day = self.days[day_name]
        current_day.add_task(task_name)


    # Liste an ToDos eines Tages zurückgeben
    def get_list_of_tasks_of_day(self, day_name):
        day = self.days[day_name]
        return day.get_tasks()
    

    def get_list_of_tasknames_of_day(self, day_name):
        day = self.days[day_name]
        return day.get_all_tasks_names()
