from Domain import Week as week

class todo_service: # Will be used by API_Client
    def __init__(self):
        self.todo_service = todo_service

    
    def create_new_week(self, c_week, month, year):
        return week.Week(c_week, month, year)