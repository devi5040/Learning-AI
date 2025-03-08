# INHERITANCE
class Animal:  # Parent class
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):  # Child class
    def bark(self):
        print("Dog barks")
d = Dog()
d.speak()  # Inherited from Animal
d.bark()   # Defined in Dog

# POLYMORPHISM
# Method overriding
class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    def speak(self):  # Overriding the method
        print("Dog barks")
class Cat(Animal):
    def speak(self):  # Overriding the method
        print("Cat meows")
animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()  # Calls the overridden method

# method overloading
class Math:
    def add(self, a, b, c=0):
        return a + b + c
m = Math()
print(m.add(2, 3))    # Uses 2 parameters
print(m.add(2, 3, 5)) # Uses 3 parameters


# ENCAPSULATION
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())
# print(acc.__balance)  # ❌ Raises an error (private variable)

# ABSTRACTION
# Implemented using abstract classes (ABC module).
from abc import ABC, abstractmethod
class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass  # Abstract method (must be overridden)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Overriding abstract method
        return 3.14 * self.radius * self.radius
c = Circle(5)
print(c.area())
