from Domain import Week as week
from Domain import Day as day
from Domain import Task as task
from Domain import day_factory

class todo_service: # Will be used by API_Client
    def __init__(self):
        # in mem storage: dict Key = calendar_week, value = week object
        # self.todo_service = todo_service
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

        if week_cal not in self.weeks_in_store.keys():
            raise KeyError("Tag konnte nicht gefunden werden!")

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

    
    # JSON
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
            
    # JSON
    def move_undone_tasks_to_next_day(self, current_day):
        correct_day = self.get_correct_day(current_day)
        undone_tasks = correct_day.get_unfinished_tasks()

        next_day = self.get_next_day(current_day)

        next_day.add_task_list_to_task(undone_tasks)
    
    
    # tag, monat, jahr
    def convert_to_date(self, some_date):
        splitted_date = some_date.split(sep=".")
        return day_factory.day_factory.create_day(int(splitted_date[2]), int(splitted_date[1]), int(splitted_date[0]))


    # JSON
    # recurrent_day = an welchem Tag soll es wiederholt werden? (String Wochentag name)
    # time_span = Für lange soll es wiederholt werden? (Anzahl Wochen für jetzt als integer)
    def add_mundane_task(self, task_name, recurrent_day, start_day, time_span):
        correct_day = self.get_correct_day(start_day)
        calendar_week = correct_day.get_week_calendar()

        the_weeks_within_time_span = [] # week objects inklusive heutige Woche

        for i in range(0, time_span):
            if calendar_week+i > 52: # Spezialfall: Ins neue Jahr übertragen
                calendar_week = 0
                the_weeks_within_time_span.append(self.weeks_in_store[calendar_week+i])
            else:
                the_weeks_within_time_span.append(self.weeks_in_store[calendar_week+i])
        
        for week in the_weeks_within_time_span:
            found_day = week.get_day(recurrent_day)
            found_day.add_task(task_name)

    #JSON
    def move_task_of_today_to_any_other_day(self, task_name, today_day, goal_day):
        correct_goal_day = self.get_correct_day(goal_day)
        correct_today = self.get_correct_day(today_day)
        tasks = correct_today.get_tasks()
        moved_task = None
        for t in tasks:
            if t.get_task_name() == task_name:
                moved_task = t
        if moved_task == None:
            raise ValueError("Aufgabe für den " + task_name + " existiert nicht!")
        else:
            correct_goal_day.add_task(task_name)
    

    def get_correct_week(self, calendar_week):
        if calendar_week not in self.weeks_in_store.keys():
            raise KeyError("Woche existiert nicht!") # Costum Exception... Es ist kein KeyError im fachlichen Sinne lol 
        return self.weeks_in_store[calendar_week]
    

    def convert_week_to_day_string(self, calendar_week):
        correct_week = self.get_correct_week(calendar_week)

        # Tupel aus (Wochentag, Formatiertes_Datum)
        string_dates = []

        days_of_week = correct_week.get_days()

        for day in days_of_week.values():
            string_dates.append((day.get_week_day().capitalize(), day.format_datetime_to_string()))
        
        return string_dates
    
    
    # Eine SubTask zu einer übergeordnete TODO an einem Tag hinzufügen
    def add_subtask_to_day(self, date, name_task, name_subtask):
        # find the correct day
        current_day = self.get_correct_day(date)
        # find the correct TODO in that day
        current_task = current_day.find_correct_task(name_task)
        # add subtask to  that TODO
        current_task.add_subtask(name_subtask)


if __name__ == "__main__":
    pass