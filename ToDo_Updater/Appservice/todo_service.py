from Domain import Week as week
from Domain import Day as day
from Domain import Task as task
from Domain import day_factory

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
    

    def get_next_day(self, current_date):
        conv_current_date = self.convert_to_date(current_date)
        week_cal = conv_current_date.get_week_calendar()
        current_week = self.weeks_in_store[week_cal]

        days_in_current_week = current_week.get_days()

        match(conv_current_date.get_week_day()):
            case "montag":
                return days_in_current_week["dienstag"]
            case "dienstag":
                return days_in_current_week["mittwoch"]
            case "mittwoch":
                return days_in_current_week["donnerstag"]
            case "donnerstag":
                return days_in_current_week["freitag"]
            case "freitag":
                return days_in_current_week["samstag"]
            case "samstag":
                return days_in_current_week["sonntag"]
            case _:
                return days_in_current_week["montag"]

    

    def get_correct_day(self, current_date):
        # find the week in which the current date is -> get calendar week of the date
        # take based on the day the suitable date object
        # add the task to the date
        conv_current_date = self.convert_to_date(current_date)
        week_cal = conv_current_date.get_week_calendar()
        current_week = self.weeks_in_store[week_cal]

         # find correct day in a week
        days_in_current_week = current_week.get_days()

        correct_day = days_in_current_week[conv_current_date.get_week_day()] # brauch den tag

        return correct_day
    

    # suppose current_date is a string
    # But do I need to store it somehwere? -> Just for one session is enough! It does not have persist 
        # I can retrieve that from Notion itself via API (GET)
        # Then the API Client can look it up under which week the current date falls 
        # Idea now: Every start: Fetch from Notion, load onto dict
    def add_task_to_day(self, task_name, current_date):
         correct_day = self.get_correct_day(current_date) 
         correct_day.add_task(task_name)

    
    # current_day is string
    def mark_task_as_done(self, task_name, current_day):
        found = False
        correct_day = self.get_correct_day(current_day)
        tasks_of_the_day = correct_day.get_tasks()
        for t in tasks_of_the_day:
            if t.get_task_name() == task_name:
                t.set_task_to_finished()
                found = True
        if(found == False):
            raise ValueError("Aufgabe nicht gefunden!")
            
    
    def move_undone_tasks_to_next_day(self, current_day):
        correct_day = self.get_correct_day(current_day)
        undone_tasks = correct_day.get_unfinished_tasks()

        next_day = self.get_next_day(current_day)

        next_day.add_task_list_to_task(undone_tasks)
    
    
    # tag, monat, jahr
    def convert_to_date(self, some_date):
        splitted_date = some_date.split(sep=".")
        return day_factory.day_factory.create_day(int(splitted_date[2]), int(splitted_date[1]), int(splitted_date[0]))
