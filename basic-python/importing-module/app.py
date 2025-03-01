import module
#importing specific items
from module import greet,number #in this case we can directly use greet and number instead of module.greet and module.number
#Using as to rename a module
import module as mod #in this case we could use mod.number instead of module.number

print(module.greet('Deviprasad'))
print(module.number)
# module is a simple python file which contains variables and functions which can be imported into other files.


# Built in modules
# 1. math
import math
print(math.sqrt(16))

# to install external package
# pip install package-name

# While working within packages we can use relative imports
# from . import module1
# from .module2 import some_function

# importlib for dynamic imports
import importlib

math_module = importlib.import_module("math")
print(math_module.sqrt(25))  # Output: 5.0
