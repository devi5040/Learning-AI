# Creating a dictionary
student = {
    "name": "Alice",
    "age": 22,
    "grade": "A"
}

# Another way using dict()
person = dict(name="John", age=30, city="New York")

# Accessing values using keys
print(student["name"])  # Output: Alice

# Using get() method (avoids KeyError)
print(student.get("age"))  # Output: 22
print(student.get("gender", "Not Found"))  # Output: Not Found

#modifying
student['age'] = 23

del student["grade"]

# Using pop()
removed_value = student.pop("subject")
print(removed_value)  # Output: Math

# Using popitem() (removes the last inserted item)
last_removed = student.popitem()
print(last_removed)  # Output: ('age', 23)

# Getting all keys
print(student.keys())  # Output: dict_keys(['name'])

# Getting all values
print(student.values())  # Output: dict_values(['Alice'])

# Getting all key-value pairs
print(student.items())  # Output: dict_items([('name', 'Alice')])

# Checking if a key exists
print("name" in student)  # Output: True

# Clearing a dictionary
student.clear()
print(student)  # Output: {}


# Iterating through keys
for key in person:
    print(key, person[key])

# Using items() to get key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")



# Creating a dictionary with squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
