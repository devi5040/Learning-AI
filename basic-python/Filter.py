# syntax => filter(function, iterable)

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

def is_even(n):
    return n % 2 == 0
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6]

# filtering strings
names = ["Alice", "Bob", "Anna", "Charlie"]
# Get names starting with 'A'
a_names = list(filter(lambda name: name.startswith("A"), names))
print(a_names)  # Output: ['Alice', 'Anna']
