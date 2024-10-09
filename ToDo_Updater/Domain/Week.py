from .Day import Day
from .Exceptions import IllegalDay
from .day_factory import day_factory as df
from datetime import timedelta, date

class Week:
    def __init__(self, day, month, year):
        try:
            self.days = {"montag": df.create_day(year, month, day), # immer den Startday angeben von jeder Woche lol
                        "dienstag": df.create_day(year, month, day).date_time + timedelta(days=1),
                        "mittwoch": df.create_day(year, month, day).date_time + timedelta(days=2),
                        "donnerstag": df.create_day(year, month, day).date_time + timedelta(days=3),
                        "freitag": df.create_day(year, month, day).date_time + timedelta(days=4),
                        "samstag": df.create_day(year, month, day).date_time + timedelta(days=5),
                        "sonntag": df.create_day(year, month, day).date_time + timedelta(days=6)
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