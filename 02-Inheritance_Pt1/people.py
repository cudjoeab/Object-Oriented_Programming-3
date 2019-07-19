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

When we call the teach method on the student instance, we get an error that
reads as follows: 'Student' object has no attribute 'teach'
We are only able to call the teach method in the Instructor class, as teaching is an instance (behaviour) of the Instructor. 
Note that the student and teacher have inherited the methods from the Person class, as they share these attributes 

""" 