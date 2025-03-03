try:
    num = int(input('Enter a number'))
    answer = 10/num
    print('The answer is:',answer)
except ZeroDivisionError:
    print('Number cannot be divisible by zero') # for input 0
except ValueError:
    print('Enter proper number') # for input 'hello'
else:
    print('The input is:',num) # if none of the above errors triggered
finally:
    print('Execution completed') # every time this code will run

# Raising exceptions manually
age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative!")
else:
    print("Your age is:", age)

# custom exceptions
class NegativeNumberError(Exception):
    pass
def check_postitive(num):
    if num<0:
        raise NegativeNumberError('Number is negative')
    return num
try:
    check_postitive(-10)
except NegativeNumberError as e:
    print('Error:',e)