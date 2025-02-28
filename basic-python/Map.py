# syntax => map(function, iterable)
numbers = [1,2,3,4]
squared_numbers = list(map(lambda x:x*x,numbers))
print(squared_numbers)


def cube(n):
    return n**3
cube_numbers = list(map(cube,numbers))
print(cube_numbers)