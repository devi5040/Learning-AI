# copy
def greet():
    print("Hello, World!")
# Copy function
greet_copy = greet  
greet_copy()  # Output: Hello, World!

# closure -> A closure is a function that remembers the variables from its enclosing scope even after the scope has finished executing.
def outer_function(msg):
    def inner_function():
        print(f"Message: {msg}")  # Uses 'msg' from outer function
    return inner_function  # Returns the inner function
closure_func = outer_function("Hello, Python!")  
closure_func()  # Output: Message: Hello, Python!

# decorator -> A decorator is a function that modifies another function without changing its actual code.
def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper  # Returns the modified function
@decorator
def say_hello():
    print("Hello, World!")
say_hello()

# decorator with arguements
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
@repeat(3)  # Run the function 3 times
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")
