class Task: 
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
    
    def __str__(self):
        return f'{self.description} due: {self.due_date}'
    
    def __repr__(self):
        return self.__str__

class TodoList: 
    def __init__(self): 
        self.tasks = []

    def add_task(self, task): 
        self.tasks.append(task) 
        
    



homework = Task('Homework', 'Friday')
laundry = Task('Laundry', 'Sunday')
groceries = Task('Get groceries', 'Saturday')

print(homework)
print(laundry)
print(groceries)

my_list = TodoList()
my_list.add_task(homework)
my_list.add_task(laundry)
my_list.add_task(groceries)

