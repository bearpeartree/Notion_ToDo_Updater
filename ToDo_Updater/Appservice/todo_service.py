from Domain import Week as week
from Domain import Day as day
from Domain import Task as task
from Domain import day_factory
import datetime

class todo_service: # Will be used by API_Client
    def __init__(self):
        self.todo_service = todo_service
        # in mem storage: dict Key = calendar_week, value = week object
        self.weeks_in_store = {}

    # expects the date of the new starting week
    def create_new_week(self, day_of_startweek, month_of_startweek, year_of_startweek):
        new_week = week.Week(day_of_startweek, month_of_startweek, year_of_startweek)
        self.weeks_in_store[new_week.get_week_calendar()] = new_week
        return new_week
    

    # Redundant?
    # Also redundant ist es nicht wirklich... die CLI darf nicht auf die Domaine direkt zugreifen
    def get_stored_weeks(self):
        return self.weeks_in_store
    

    # suppose current_date is a string
    # But do I need to store it somehwere? -> Just for one session is enough! It does not have persist 
        # I can retrieve that from Notion itself via API (GET)
        # Then the API Client can look it up under which week the current date falls 
        # Idea now: Every start: Fetch from Notion, load onto dict
    def add_task_to_day(self, task_name, current_date):
         # find the week in which the current date is -> get calendar week of the date
         # take based on the day the suitable date object
         # add the task to the date
         conv_current_date = self.convert_to_date(current_date)
         print(type(conv_current_date))
         week_cal = conv_current_date.get_week_calendar()
         current_week = self.weeks_in_store[week_cal]


         # find correct day in a week
         days_in_current_week = current_week.get_days()
        #  for d in days_in_current_week:
        #      print(type(days_in_current_week[d]))
         correct_day = days_in_current_week[conv_current_date.get_week_day()] # brauch den tag
         correct_day.add_task(task_name)

    
    
    # tag, monat, jahr
    def convert_to_date(self, some_date):
        splitted_date = some_date.split(sep=".")
        return day_factory.day_factory.create_day(int(splitted_date[2]), int(splitted_date[1]), int(splitted_date[0]))
