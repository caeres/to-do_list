#class in extra file - no idea whether thats best practice or not

class ToDo:
    def __init__(self, due_to, task):
        self.due_to = due_to
        self.task = task
    def __repr__(self):
        return f"To Do({self.due_to!r}, {self.task!r})"
    def __str__(self):
        return f"{self.due_to}: {self.task}"
    #getter functions
    def get_task(self):
        return self.task
    def get_due_to(self):
        return self.due_to

#OBSOLETE prolly
    #prints due_date and task in "Date: Task" format (as a string)
    #def print_info(self):
    #   return f"{self.get_due_to()}: {self.get_task()}"

