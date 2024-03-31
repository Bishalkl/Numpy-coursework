# Great! Practicing is an excellent way to solidify your understanding of NumPy. Below are some practice exercises and tasks that you can work on to enhance your skills with NumPy:


# ### Exercise 3: Array Slicing and Indexing

# 1. Extract all the odd numbers from an array.
# 2. Reverse the rows of a 2D array.
# 3. Extract the diagonal elements of a 3x3 matrix.

# ### Exercise 4: Array Manipulation

# 1. Reshape a 1D array into a 3x3 matrix.
# 2. Flatten a 2D array into a 1D array.
# 3. Stack two 1D arrays vertically and horizontally.

# ### Exercise 5: Mathematical Functions

# 1. Compute the mean, median, and standard deviation of an array.
# 2. Find the minimum and maximum values in an array.
# 3. Normalize a given array (subtract the mean and divide by the standard deviation).

# ### Exercise 6: Advanced Operations

# 1. Find the unique elements in an array.
# 2. Sort an array in ascending and descending order.
# 3. Replace all negative values in an array with 0.

# ### Exercise 7: Random Number Generation

# 1. Generate a 1D array with 10 random integers between 1 and 100.
# 2. Create a 3x3 matrix with random values sampled from a standard normal distribution.
# 3. Shuffle the elements of a 1D array.

# ### Exercise 8: File Operations

# 1. Save an array to a text file.
# 2. Load an array from a text file.

# ### Exercise 9: Linear Algebra

# 1. Compute the eigenvalues and eigenvectors of a matrix.
# 2. Solve a system of linear equations.
# 3. Compute the matrix inverse.

# ### Exercise 10: Boolean Indexing

# 1. Find all the elements greater than a certain value in an array.
# 2. Count the number of elements less than a certain value in an array.
# 3. Extract elements from an array based on a condition.



# ### Exercise 1: Create NumPy Arrays

# 1. Create a 1D array with values ranging from 0 to 9.
# 2. Create a 3x3 matrix with values ranging from 0 to 8.
# 3. Create a 5x5 identity matrix.

import numpy as np
# 1
a = np.arange(10)
print(a)

# 2 
a1 = np.arange(9).reshape(3,3)
print(a1)

# 3 
a2 = np.eye(5) #to create an identity matrix
print(a2)


# ### Exercise 2: Array Operations

# 1. Add two 2D arrays element-wise.
# 2. Multiply two 2D arrays element-wise.
# 3. Compute the dot product of two 2D arrays.


import numpy as np


t1 = np.array([[1,2,3,4],
               [1,2,3,5]])
t2 = np.array([[2,3,2,3],
               [1,2,4,3]])

#1
print(t1 + t2)

#2
print(t2 * t1)

#3
# s1 = np.dot(t1,t2)
# print(s1) #using dot function
# print( t1 @ t2) #using operator '@'

# ### Exercise 3: Array Slicing and Indexing

# 1. Extract all the odd numbers from an array.
# 2. Reverse the rows of a 2D array.
# 3. Extract the diagonal elements of a 3x3 matrix.

#1
t3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 18, 57, 36, 10, 36])
for i in range(len(t3)-1, -1, -1):
    if t3[i] % 2 != 0:
        t3 = np.delete(t3, i)
print(t3)

#2 
t4 = np.array([[1,2,3],
               [2,4,3]])
print(t4[::-1])

#3










