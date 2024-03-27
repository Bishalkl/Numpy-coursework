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
             [4,7,"Hello"]])

print(e.dtype) #it will give object because it has object data within e variable

print(e)

#filling arrays

# full function
f = np.full((2,3,4), 9)
print(f) #this allows to full the arrays of value accroding with user input 

#zeros function, it is similar but with full of zeros in arrays.

#ones function, it is similar but with full of 1's in arrays.

#empty function, it is also similar but with with allocating the memory on it.

# arange function , it is allows use to get a range value according to the user
x_value = np.arange(0,50, 5)
print(x_value)

# linspace function, it allows and divided gap between range of number given.
y_value = np.linspace(0, 500, 10)
print(y_value)

#nan and inf, it's mostly use when data set is null value 

#nan
print(np.isnan(np.nan)) # nan non number

#inf
print(np.isinf(np.inf)) #it is infinity


#Mathmatical operation, while list will add as string but in numpy arrays do the operation according to vector and matricxs.
l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]

a1 = np.array(l1)
a2 = np.array(l2)

print(l1 + l2) # output is [1, 2, 3, 4, 5, 3, 4, 5, 6, 7]
print(a1 + a1) # output is [ 2  4  6  8 10]

# operation in different dimension, under some condition if one of the dimension is similar

# sqrt, it will allows to squre the number in numpyarrays
l3 = np.array([1,2,3,4,5])

# some important function
print(np.sqrt(l3))
print(np.sin(l3))
print(np.cos(l3))
print(np.log10(l3))


#Array method
print(np.append(l3,[1,2,3])) # it will append value according the user how we arange that.
print(np.insert(l3,2,[1,2,3])) # it will insert the value according to the index address.
print(np.delete(l3,1)) # it will delete value according to the index we given, we can also use in multiple column with multiple index according the arrangement in function









 












