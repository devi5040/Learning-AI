#1. if statements
x = 10
if x>7:
    print(x,' is greater than 7')

#2. if-else statements
x = 10
if x>5:
    print(x,' is greater than 5')
else:
    print(x, ' is less than 5')

#3. if-elif-else
x=11
if x%2==0:
    print(x, ' is an even number')
elif x%2!=0:
    print(x, ' is an odd number')
else:
    print(x, ' is not a number')

#4. combined with logical operators
x=1
if x>0 and x<10:
    print(x, ' is greater than 0 and less than 10')

# pass statements
# if we want to skip any condition we can use pass
x = 3
if x==3:
    pass