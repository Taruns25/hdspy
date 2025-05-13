import numpy as np
'''
a = np.array([[1,2,3],[4,5,6]])  #creates a 2d array
print(a.ndim)                         # returns the dimension of the array
print(a.dtype)                        # returns th type of data in the array
print(a.size )                        # returns the size of the matrix 2x3 , 3x3
print(a.shape)                        # returns the shape (2,3) (3,3)...
zeros = np.zeros((2,3))          # creates an array of zeros of the given size
ones = np.ones((3,3))            # creates an array of ones of the given size
ranged = np.arange(0, 11, 2)     # creates a 1D array of evenly spaced numbers between 0 and 10 (excluding 10), stepping by 2.
matrix = ranged.reshape((2,3))   # reshapes an given into the specified shape , but must have enough elements
print(ranged) 
print(matrix)
'''
arr = np.random.rand(3,3)
print(arr)
np.mean(arr)
np.max(arr)
np.median(arr)
mul = arr*10
print(arr[:1])
flat=arr.flatten()

