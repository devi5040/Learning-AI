# 1. Numeric
# integers
x=10
y=-8

# float
a=0.7
b=-6.0

# Complex Numbers
num = 2 + 3j
print(type(num))  # Output: <class 'complex'>

# 2. Boolean
x=True
y= False

# 3. String types
name = "devi"
x='hello'
multiline = '''This is a 
multiline string'''

# 4. Sequence Types
# Lists => mutable, ordered
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adding an item
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
print(type(fruits))  # Output: <class 'list'>

#Tuple => immutable, ordered
colors = ("red", "green", "blue")
print(colors[0])  # Output: red
print(type(colors))  # Output: <class 'tuple'>

# 5. Set Types
# set => mutable, unordered, unique
my_set = {1, 2, 3, 4, 4}  # Duplicate 4 is ignored
print(my_set)  # Output: {1, 2, 3, 4}
print(type(my_set))  # Output: <class 'set'>

#frozenset => immutable set
fs = frozenset([1, 2, 3, 4])
print(type(fs))  # Output: <class 'frozenset'>

# 6. Dictionary types
student = {"name": "Alice", "age": 25, "city": "New York"}
print(student["name"])  # Output: Alice
print(type(student))  # Output: <class 'dict'>

# 7. None type
x = None
print(type(x))  # Output: <class 'NoneType'>
