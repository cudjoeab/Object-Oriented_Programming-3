class Person: 
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'Hi, my name is {self.name}!'


class Instructor(Person): 
    def teach(self): 
        return f'An object is an instance of a class.'


class Student(Person): 

    def learn(self):
        return f'I get it!'


nadia = Instructor('Nadia')
chris = Student('Chris')


print(chris)
print(nadia)

print(nadia.teach())
print(chris.learn())
print(chris.teach())

"""
Comment on calling the teach method on student instance:

We cannot call the teach instance method on chris because chris is an instance of Student, which does not have a teach instance method. 

""" 