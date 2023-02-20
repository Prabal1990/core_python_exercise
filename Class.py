class Dog:
    """A simple attempt to model a dog."""
    """"__init__() method- Python runs automatically"""
    def __init__(self, name, age):
        """Initialize name and age attributes.
        self is passed automatically, so we don’t need to pass it.
        we'll provide values for only the last two parameters"""
        self.name = name #output name is variable, name in method is parameter
        # name takes the value associated with the parameter name
         # and assigns it to the variable name
        self.age = age
 
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Wille', 10)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
your_dog = Dog('German Seferd', 6)
your_dog.sit()
your_dog.roll_over()
her_dog = Dog('German Seferd', 6)
her_dog.sit()
her_dog.roll_over()

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        # whatever inside the method is call attibute
        self.make = make
        self.model = model
        self.year = year
        self.adometer_reading = 0
 
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"Our car start with the mileage of {self.adometer_reading}")
    def update_odometer(self, mileage):
        self.adometer_reading= mileage
    
my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())
my_new_car.adometer_reading = 21
#changing audometer reading
print(my_new_car.read_odometer())
print(my_new_car.update_odometer(23))
print(my_new_car.read_odometer())
