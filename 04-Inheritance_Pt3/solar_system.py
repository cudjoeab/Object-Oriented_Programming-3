class System: 
    def __init__(self):
        self.bodies = []
    
    def add(self, body):
        self.bodies.append(body)

    def total_mass(self):
        total = 0
        for body in self.bodies: 
            total += body
            return total 
    
class Body: 
    def __init__(self, name, mass): 
        self.name = name
        self.mass = mass 

class Planet(Body):
    def __init__(self, name, mass, day, year):
        super().__init__(name, mass)
        self.day = day 
        self.year = year 

class Star(Body):
    def __init__(self, name, mass, star_type):
        super().__init__(name, mass)
        self.star_type = star_type 


class Moon(Body):  
    def __init__(self, name, mass, month, planet):  
        super().__init__(name, mass)
        self.month = month
        self.planet = planet

earth = Planet('Earth', 5.97, 24, 365) 
sun = Star('Sun', 1.89, 'G2V')
moon = Moon('Moon', 7.35, 27, earth)

print(moon)

solar_system = System()
solar_system.add(earth)
solar_system.add(moon)
solar_system.add(sun)

print(solar_system.bodies)


## STRETCH: create a string dunder in the System method to be able to see the items in the list











