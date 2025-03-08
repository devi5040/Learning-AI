# __iter__() -> Returns the iterator object itself.
# __next__() -> Returns the next value in the sequence; raises StopIteration when finished.
# An object that can return an iterator -> iterable.	An object that can be iterated upon -> iterator

# custom iterator
class Squares:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 1
    def __iter__(self):
        return self  # Returns itself as an iterator
    def __next__(self):
        if self.current > self.max_num:
            raise StopIteration  # End of iteration
        result = self.current ** 2
        self.current += 1
        return result
squares = Squares(5)  # Create an iterator
for num in squares:
    print(num)  # Output: 1, 4, 9, 16, 25

# sentinel iteration it stops when a certain value is encountered
import random
def random_numbers():
    return random.randint(1, 10)
iterator = iter(random_numbers, 5)  # Stop when 5 is generated
for num in iterator:
    print(num)

# infinite iterators
from itertools import count
for num in count(10, 2):  # Start at 10, step by 2
    print(num)
    if num > 20:
        break  # Prevent infinite loop

# generators a simple way to create iterators
def squares_generator(n):
    for i in range(1, n + 1):
        yield i ** 2  # Yield returns values one at a time
squares = squares_generator(5)
print(next(squares))  # Output: 1
print(next(squares))  # Output: 4

# using loop instead of next()
for num in squares(5):
    print(num)  # Output: 1, 4, 9, 16, 25

# infinite generators
def infinite_counter():
    num = 1
    while True:
        yield num
        num += 1
counter = infinite_counter()
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2

# Reading large files
def read_large_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()  # Read one line at a time
for line in read_large_file("data.txt"):
    print(line)  # Efficiently reads the file without loading everything into memory
