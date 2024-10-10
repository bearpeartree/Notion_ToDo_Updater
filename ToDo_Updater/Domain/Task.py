class Task:
    def __init__(self, task_name, associated_day):
        self.task_name = task_name
        self.associated_day = associated_day
        self.finished = False

    def get_task_name(self):
        return self.task_name
    
    def get_associated_day(self):
        return self.associated_day
    
    def is_finished(self):
        return self.finished
    
    def set_task_to_finished(self):
        self.finished = True