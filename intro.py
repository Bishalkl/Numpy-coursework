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

#structuring method, this method able to changee the shape 
l4 = np.array([[1,2,3,4,7],
               [2,3,4,6,7],
               [2,4,6,2,6],
               [2,3,3,6,6]])

print(l4.shape)

import numpy as np

# Original array
l4 = np.array([[1,2,3,4,7],
               [2,3,4,6,7],
               [2,4,6,2,6],
               [2,3,3,6,6]])

# Displaying the shape of the array
print(l4.shape)  # Output: (4, 5)

# Reshaping the array
# Reshape function - we can only reshape according to the available values; 
# we can't reshape to a shape that is not compatible with the original number of elements
print(l4.reshape((1,1,1,1,2,10)))  

# Flatten the array
print(l4.flatten())  # Output: [1 2 3 4 7 2 3 4 6 7 2 4 6 2 6 2 3 3 6 6]

# Loop through flattened array
var = [v for v in l4.flat]
print(var)  # Output: [1, 2, 3, 4, 7, 2, 3, 4, 6, 7, 2, 4, 6, 2, 6, 2, 3, 3, 6, 6]

# Transpose the array
print(l4.T)

# Swap axes of the array
print(l4.swapaxes(0,1))  # Swap rows and columns


# concatenating
b1 = np.array([[1,2,3,4],
               [3,4,5,7]])

b2 = np.array([[1,2,3,0],
               [3,4,5,1]])

b3 = np.concatenate((b1,b2), axis=0)
b4 = np.concatenate((b1,b2), axis=1)

print(b3)
print(b4)

#stacking, it similar but in new dimension create
b5 = np.stack((b1,b2))
b6 = np.vstack((b1,b2)) # act like 0 axis of concatenate
b7 = np.hstack((b1,b2)) # act like 1 axis of cocatenate
print(b5)
print(b6)
print(b7)


#split it is use to divide the single array in multiple 
b8 = np.array([[1,2,3,4,6],
               [2,3,4,5,7],
               [5,4,3,6,5],
               [7,5,3,6,8]])

print(np.split(b8, 4, axis=0)) # it will divide the split in rows axis
print(np.split(b8, 5, axis=1)) #it will divide the split in column axis

#aggregate function
print(b8.max())
print(b8.min())
print(b8.mean())
print(b8.std())
print(b8.sum())
print(np.median(b8))

#Numpy randoms
b9 = np.random.randint(0, 1, size=(2,3,4))
print(b9)
b10 = np.random.binomial(10, p=0.5, size=(3,4))
print(b10)
b11 = np.random.choice([3,2], size=(5,10))
print(b11)

#Exporting and importing

np.save("myarray.npy", b8)

np.savetxt("myarray.csv", b8, delimiter=",")

b12 = np.loadtxt("myarray.csv", delimiter=",")
print(b12)





















 












