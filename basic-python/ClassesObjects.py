class Car:
    # The __init__ method is a constructor that gets called automatically when a new object is created.
    def __init__(self, brand, model):
        self.brand = brand  # Instance Variable
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

# Creating an object of the class
my_car = Car("Toyota", "Corolla")
my_car.display_info()

# class and instance variables
class Employee:
    company = "TechCorp"  # Class variable

    def __init__(self, name, salary):
        self.name = name      # Instance variable
        self.salary = salary  # Instance variable

e1 = Employee("John", 50000)
print(e1.name, e1.salary, e1.company)

#class methods => It takes cls as the first parameter instead of self.
class School:
    school_name = "Greenwood High"

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

School.change_school("Sunrise Academy")
print(School.school_name)

# static method => It doesn’t use self or cls. It behaves like a regular function but is placed inside a class for organizational purposes.
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
print(MathOperations.add(5, 3))
