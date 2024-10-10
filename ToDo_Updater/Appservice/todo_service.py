from Domain import Week as week
from Domain import Day as day
from Domain import Task as task
import datetime

class todo_service: # Will be used by API_Client
    def __init__(self):
        self.todo_service = todo_service
        # in mem storage: dict Key = calendar_week, value = week object
        self.weeks_in_store = {}

    # expects the date of the new starting week
    def create_new_week(self, day_of_startweek, month_of_startweek, year_of_startweek):
        new_week = week.Week(day_of_startweek, month_of_startweek, year_of_startweek)
        self.weeks_in_store[new_week.get_week_calendar] = new_week
        return new_week
    

    def get_stored_weeks(self):
        return self.weeks_in_store
    

    # suppose current_date is a string
    # But do I need to store it somehwere? -> Just for one session is enough! It does not have persist 
        # I can retrieve that from Notion itself via API (GET)
        # Then the API Client can look it up under which week the current date falls 
        # Idea now: Every start: Fetch from Notion, load onto dict
    def add_task_to_day(task_name, current_date):
         # find the week in which the current date is -> get calendar week of the date
         # take based on the day the suitable date object
         # add the task to the date
         #current_date_obj = convert_to_date(current_date)
         pass
    
    
    # tag, monat, jahr
    def convert_to_date(self, some_date):
        splitted_date = some_date.split(sep=".")
        return datetime.datetime(int(splitted_date[2]), int(splitted_date[1]), int(splitted_date[0]))
