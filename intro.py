# Importing the numpy library with alias np
import numpy as np

# Creating a numpy array
a = np.array([1, 2, 3, 4, 5])

# Printing the numpy array
print(a)

# Checking the type of the numpy array
print(type(a))

# Python list manipulation is similar in numpy arrays
# Example:
print(a[1])  # Output is 2
print(a[1:])  # Output is [2 3 4 5]
print(a[:3])  # Output is [1 2 3]

# Modifying values in the numpy array
a[2] = 10
print(a)  # Output is [1 2 10 4 5]

# Creating a multi-dimensional numpy array
a_mul = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(a_mul)  # Output is [[1 2 3]
              #           [4 5 6]
              #           [7 8 9]]

# Fundamental functions and attributes of numpy arrays
# Checking the shape (dimensions) of the array
print(a_mul.shape)  # Output is (3, 3)

# Checking the number of dimensions
print(a_mul.ndim)  # Output is 2

# Checking the total number of elements
print(a_mul.size)  # Output is 9

# Checking the data type of elements
print(a_mul.dtype)  # Output is int64

# data type 
b = np.array([[1,2,3],
              ["3",1,"5"],
              [7,8,9]], dtype=np.float32) #we can cast datatype

print(b.dtype) # output is <u21 mean it is a mixed data type even we access seperately it will say string datatype

d = {'1': "bishal"}

e = np.array([[1,2,3],
             [d,1,6],
             [4,7,6]])

print(e.dtype) #it will give object because it has object data within e variable














