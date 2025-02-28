# syntax => lambda arguments: expression

add = lambda a, b: a + b
print(add(3, 4))  # Output: 7

# lambda inside a function
def multiplier(n):
    return lambda x: x * n
double = multiplier(2)
print(double(5))  # Output: 10

