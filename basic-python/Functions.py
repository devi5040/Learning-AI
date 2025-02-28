def greet(name="john"):
    print(f"Hello ${name}")
greet('patel')
greet()

# Using keyword arguments
def student_info(name, age):
    print(f"Name: {name}, Age: {age}")
student_info(age=22, name="Bob")

#using *args
def add(*args):
    return sum(args)
num_sum = add(1,2,3,4)

#using **kwargs
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
show_info(name="Alice", age=22, city="New York")
