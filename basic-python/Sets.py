# Creating a set
my_set = {1, 2, 3, 4, 5}

# Creating an empty set (must use set(), not {})
empty_set = set()

# Creating a set with duplicate values (duplicates are removed)
unique_numbers = {1, 2, 2, 3, 4, 4, 5}
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

print(3 in my_set)  # Output: True
print(10 in my_set)  # Output: False

# Adding a single element
my_set.add(6)

# Adding multiple elements
my_set.update([7, 8, 9])

# Removing an element (raises KeyError if not found)
my_set.remove(3)

# Removing an element safely (no error if not found)
my_set.discard(10)

# Removing and returning a random element
removed = my_set.pop()
print(removed)

# Clearing all elements
my_set.clear()

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (all unique elements from both sets)
print(A | B)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection (common elements)
print(A & B)  # Output: {3, 4}

# Difference (elements in A but not in B)
print(A - B)  # Output: {1, 2}

# Symmetric Difference (elements in either A or B but not both)
print(A ^ B)  # Output: {1, 2, 5, 6}


set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.intersection(set2))  # Output: {3}
print(set1.difference(set2))  # Output: {1, 2}
print(set1.issubset(set2))  # Output: False
print(set1.issuperset(set2))  # Output: False
