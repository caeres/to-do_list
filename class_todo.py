#class in extra file - seems to be best practice (prolly missing something tho)

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
    
    #managing todos
    def check_equal(self, other_todo):
        if (self.due_to == other_todo.due_to 
        and self.task == other_todo.task):
            return True
        else:
            return False
    
