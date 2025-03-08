# overloading +
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"Point({self.x}, {self.y})"
p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2  # Uses __add__
print(p3)  # Output: Point(6, 8)

# overloading - 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
p1 = Point(6, 8)
p2 = Point(2, 3)
p3 = p1 - p2  # Uses __sub__
print(p3)  # Output: Point(4, 5)

# overloading *
class Number:
    def __init__(self, value):
        self.value = value
    def __mul__(self, other):
        return Number(self.value * other.value)
    def __str__(self):
        return str(self.value)
n1 = Number(4)
n2 = Number(3)
n3 = n1 * n2  # Uses __mul__
print(n3)  # Output: 12

# overloading == 
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __eq__(self, other):
        return self.price == other.price
p1 = Product("Laptop", 1000)
p2 = Product("Tablet", 800)
p3 = Product("Phone", 1000)
print(p1 == p2)  # Output: False
print(p1 == p3)  # Output: True

# overloading < >
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __lt__(self, other):  # Less than `<`
        return self.price < other.price
    def __gt__(self, other):  # Greater than `>`
        return self.price > other.price
p1 = Product("Laptop", 1000)
p2 = Product("Tablet", 800)
print(p1 > p2)  # Output: True
print(p1 < p2)  # Output: False

# overloading /
class Number:
    def __init__(self, value):
        self.value = value
    def __truediv__(self, other):  # For `/`
        return Number(self.value / other.value)
n1 = Number(10)
n2 = Number(2)
n3 = n1 / n2  # Uses __truediv__
print(n3)  # Output: 5.0

#overloading %
class Number:
    def __init__(self, value):
        self.value = value
    def __mod__(self, other):
        return Number(self.value % other.value)
n1 = Number(10)
n2 = Number(3)
n3 = n1 % n2  # Uses __mod__
print(n3)  # Output: 1

# overloading //
class Number:
    def __init__(self, value):
        self.value = value
    def __floordiv__(self, other):
        return Number(self.value // other.value)
n1 = Number(10)
n2 = Number(3)
n3 = n1 // n2  # Uses __floordiv__
print(n3)  # Output: 3

# overloading +=
class Number:
    def __init__(self, value):
        self.value = value
    def __iadd__(self, other):  # In-place addition `+=`
        self.value += other.value
        return self
n1 = Number(5)
n2 = Number(3)
n1 += n2  # Uses __iadd__
print(n1)  # Output: 8

# overloading str and repr
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def __str__(self):  # User-friendly output
        return f"{self.brand} costs ${self.price}"
    def __repr__(self):  # Debugging representation
        return f"Car('{self.brand}', {self.price})"
car = Car("Tesla", 50000)
print(str(car))   # Output: Tesla costs $50000
print(repr(car))  # Output: Car('Tesla', 50000)
