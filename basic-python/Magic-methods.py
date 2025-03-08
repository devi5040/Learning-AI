# __init__ -> initializes an object (constructor)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p = Person("Alice", 25)
print(p.name)  # Alice
print(p.age)   # 25

# __str__ -> returns a readable string representation (str(obj))
# __repr__ -> returns an unambiguous string representation (repr(obj))
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"
p = Person("Alice", 25)
print(str(p))   # Person(name=Alice, age=25)
print(repr(p))  # Person('Alice', 25)

# __len__ -> defines behavior for len(obj)
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    def __len__(self):
        return self.pages
b = Book("Python Basics", 300)
print(len(b))  # 300

# __call__ -> allows an object to be called like a function
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    def __call__(self, number):
        return number * self.factor
double = Multiplier(2)
print(double(5))  # 10

# __getitem__ -> Enables indexing obj[key]
# __setitem__ -> Sets a value using obj[key]=value
# __delitem__ -> deletes an item del obj[key]
class CustomList:
    def __init__(self):
        self.data = {}
    def __getitem__(self, key):
        return self.data.get(key, "Key not found")
    def __setitem__(self, key, value):
        self.data[key] = value
    def __delitem__(self, key):
        del self.data[key]
cl = CustomList()
cl["name"] = "Alice"  # __setitem__
print(cl["name"])     # __getitem__ → Alice
del cl["name"]        # __delitem__
print(cl["name"])     # Key not found

# __add__ -> defines behavior for + operator
# __sub__ -> defines behavior for - operator
# __mul__ -> defines behavior for * operator
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __str__(self):
        return f"Point({self.x}, {self.y})"
p1 = Point(2, 3)
p2 = Point(4, 5)
print(p1 + p2)  # Point(6, 8)
print(p1 - p2)  # Point(-2, -2)

# __eq__ -> defines behavior for == operator
# __lt__ -> defines behavior for < operator
# __gt__ -> defines behavior for > operator
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __eq__(self, other):
        return self.price == other.price
    def __lt__(self, other):
        return self.price < other.price
p1 = Product("Laptop", 1000)
p2 = Product("Tablet", 800)
print(p1 == p2)  # False
print(p1 < p2)   # False (1000 < 800)
print(p1 > p2)   # True

# __enter__ and __exit__ -> Enables with statement (context manager)
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
with FileHandler("test.txt") as f:
    f.write("Hello, world!")
# File is automatically closed after the `with` block
