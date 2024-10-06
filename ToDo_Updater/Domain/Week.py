class Week:
    def __init__(self, calendar_week, month):
        self.days = []
        self.calendar_week = calendar_week
        self.month = month

    def get_calendar_week(self):
        return self.calendar_week
    
    def get_month(self):
        return self.month