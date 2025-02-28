# Lists in python
# ordered, mutable and can contain different data types
# List of strings
fruits = ['mango','apple','pineapple']
# List with different types of data
difdata = [1, 'mango',2.3]
#nested list
data = [[2,3,5],[1,4,6]]

#accessing list elements
print(difdata[0])  #1
print(difdata[-1]) #2.3
print(difdata[0:2]) #1 mango
#modifying the list 
difdata[0] = 2
print(difdata) #2 mango 2.3

# List methods
fruits.append('chiku') #adds chiku at the end
fruits.insert(2, 'orange') #inserts orange at postion 2
fruits.remove('mango') #removes the element
fruits.pop()  #removes the last element
fruits.sort() # sorts the list
fruits.reverse() #reverse the list

# List Comprehension
# Concise way to create lists in python. It makes the code more readable and efficient.
squares = [x**2 for x in range(1,6)]
print(squares)  #[1, 4, 9, 16, 25]

#for even numbers
even = [x for x in range(1, 11) if x%2==0]
print(even) #[2, 4, 6, 8, 10]

#converting list of strings to uppercase
uppercase = [fruit.upper() for fruit in fruits]
print(uppercase) #['PINEAPPLE', 'ORANGE', 'APPLE']

# Creating a list of tuples (number, square)
squares_tuple = [(x, x**2) for x in range(1, 6)]
print(squares_tuple)  # Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]