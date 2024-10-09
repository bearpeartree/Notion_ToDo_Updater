from Domain import Week as week
from Domain import Day as day
from Domain import Task as task

class todo_service: # Will be used by API_Client
    def __init__(self):
        self.todo_service = todo_service

    # expects the date of the new starting week
    def create_new_week(self, day_of_startweek, month_of_startweek, year_of_startweek):
        return week.Week(day_of_startweek, month_of_startweek, year_of_startweek)
    

    # suppose current_date is a string
    # But do I need to store it somehwere? -> Just for one session is enough! It does not have persist
    def add_task_to_day(task_name, current_date):
         # find the week in which the current date is => Calculate the 
         # take based on the day the suitable date object
         # add the task to the date
         pass
