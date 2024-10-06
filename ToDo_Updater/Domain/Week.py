from . import Day

class Week:
    def __init__(self, calendar_week, month):
        self.days = [Day("Montag", calendar_week), 
                    Day("Dienstag", calendar_week),
                    Day("Mittwoch", calendar_week),
                    Day("Donnerstag", calendar_week),
                    Day("Freitag", calendar_week),
                    Day("Samstag", calendar_week),
                    Day("Sonntag", calendar_week)]
        self.calendar_week = calendar_week
        self.month = month

    def get_calendar_week(self):
        return self.calendar_week
    
    def get_day(self, day_name):
        index = self.days.index(day_name)
        return self.days[index]
    
    def get_month(self):
        return self.month