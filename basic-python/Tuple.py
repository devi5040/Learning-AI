my_tuple = ('hello', 1, 3)

single_element_tuple = (23, ) # comma is required

# Without parentheses (tuple packing)
another_tuple = 10, 20, 30  

# accessing tuple elements
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:2])

#concatenation
tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple_output = tuple1+tuple2
print(tuple_output) #1,2,3,4,5,6

tuple3 = (1,2,3)*3
print(tuple3) # (1, 2, 3, 1, 2, 3, 1, 2, 3)

print(2 in tuple3) # True

numbers = (1,2,3,4,5,2,3)
print(numbers.count(2)) # 2
print(numbers.index(2)) # 3

coordinates = (10, 20, 30)
x, y, z = coordinates  # Unpacking tuple into variables
print(x, y, z)  # Output: 10 20 30
