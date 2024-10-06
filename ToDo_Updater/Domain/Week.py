from .Day import Day

class Week:
    def __init__(self, calendar_week, month):
        self.days = [Day("Montag", calendar_week), 
                    Day("Dienstag", calendar_week),
                    Day("Mittwoch", calendar_week),
                    Day("Donnerstag", calendar_week),
                    Day("Freitag", calendar_week),
                    Day("Samstag", calendar_week),
                    Day("Sonntag", calendar_week)]
        if calendar_week >= 1 and calendar_week <= 52:
            self.calendar_week = calendar_week
        else:
            raise ValueError("Kalenderwoche darf nur von 1 bis 52 sein!")
        self.month = month


    def get_calendar_week(self):
        return self.calendar_week
    

    def get_day(self, day_name):
        for i in self.days:
            if i.get_day() == day_name:
                return i
        raise ValueError("Der Tag existiert nicht.")
    

    def get_month(self):
        return self.month