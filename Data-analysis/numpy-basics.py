import numpy as np

a=np.array([(1,2,3),(4,5,6)])
b=np.array([1,2,3,4,5,6])
c = np.array([[1,2,3],[4,5,6]])
print(a)
print(b)
print(c)

# properties
print(c.shape) # (2,3) -> (row, column)
print(b.dtype)  # int64 -> type of the data
print(a.ndim)   # 2 -> number of dimensions
print(c.size)   # 6 -> size of the array

# creating special arrays
d = np.zeros((3,3)) # zeros array
e = np.ones((2,3))  # ones array
f = np.full((2,2),5)    # array with size 2*2 and each element is 5
g = np.eye(3) # identity matrix 3*3
h = np.arange(1,10,2) # arrays with range of numbers (start, stop, step)
i = np.linspace(1,5,10) # 10 numbers evenly spaced between 1 and 5
j = np.random.rand(3,3) # random numbers between 0 and 1, in size 3*3
k = np.random.randint(1,100,(2,3))  # 2x3 matrix with random integers between 1 and 100
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)

# indexing and slicing
l = np.array([10, 20, 30, 40, 50])
print(l[0])   # 10
print(l[-1])  # 50
m = np.array([10, 20, 30, 40, 50])
print(m[1:4])    # [20 30 40] -> Slicing from index 1 to 3
print(m[:3])     # [10 20 30] -> First three elements
print(m[-3:])    # [30 40 50] -> Last three elements

# Arithmetic operations
n = np.array([[1,2],[3,4]])
print(n*3)
print(n*-1)

# Matrix Operations
o = np.array([[1,2],[3,4]])
p = np.array([[4,5],[6,7]])
print(o*p) # element wise multiplication
print(np.dot(o,p))  # matrix multiplication

# statistical operations
q = np.array([1,2,3,4,5,6])
print(np.mean(q)) # mean
print(np.median(q)) # median
print(np.std(q))    # standard deviation
print(np.var(q))    # Variance
print(np.min(q))    # minimum
print(np.max(q))    # maximum

# Reshaping the array
r = np.array([1,2,3,4,5,6])
r_reshape = r.reshape(2,3)
print(r_reshape)

# Flattening
s = np.array([[1,2,3],[4,5,6]])
print(s.flatten())

# stacking
t = np.array([1,2,3])
u = np.array([4,5,6])
print(np.vstack((t,u)))
print(np.hstack((t,u)))

# splitting
v = np.array([1, 2, 3, 4, 5, 6])
print(np.split(v, 3))  # Splits into 3 arrays: [1,2], [3,4], [5,6]

# boolean indexing and filtering
arr = np.array([10, 20, 30, 40, 50])
print(arr[arr > 25])  # [30 40 50] -> Filters values greater than 25

# copying vs view
arr = np.array([1, 2, 3])
# Copy (independent array)
copy_arr = arr.copy()
copy_arr[0] = 100
print(arr)  # Original remains unchanged
# View (linked array)
view_arr = arr.view()
view_arr[0] = 100
print(arr)  # Original changes as well

# saving and loading numpy array
arr = np.array([1, 2, 3, 4, 5])
# Saving
np.save('my_array.npy', arr)
# Loading
loaded_arr = np.load('my_array.npy')
print(loaded_arr)