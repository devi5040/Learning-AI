# Variables declaration in python
x = 10 #integer
name = "Alice"  # String
price = 99.99  # Float
is_active = True  # Boolean

# Multiple Assignments
a,b,c=10,20,30 #a=10, b=20, c=30
x=y=z=100

#Dynamic typing
x=10
x='hello' #variables  can change types at runtime

# Global vs Local
x=10 #global
def fun():
    x=23  #local
fun()
#modifying global variable inside function
x=10
def fun():
    global x
    x=23
fun()

#deleting a variable
a=10
del a