import numpy as np
arr=np.array([2,5,6,8])
print(arr)
print(type(arr))
#Creating 0D array #  Dimension is also called as scalar.
arr1=np.array(69)
print(arr1)
print(type(arr1))
#Creating 1D array.   1 Dimension is also called as vector
#Variable arr is the example of 1 dimension array
print(arr1.ndim)#.ndim is the function to check the dimension of the array where
#n is the no. , and dim stands for the dimension
#Creating 2 Dimension array
arr2=np.array([[5,6,8],[2,5,6]])
print(arr2)
print(arr2.ndim)
arr4=np.array([1,2,3,4,5,],ndmin=10)#Creating an array with 10 dimension
print(arr4)
print(arr4.ndim)
