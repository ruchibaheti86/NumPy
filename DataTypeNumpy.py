import numpy as np
#Data Type In Numpy: dtype
arr = np.array([1,2,3,4])
print("Array: ",arr)
print("Data Type in Array: ")
print(arr.dtype)

arr = np.array(['Apple', 'Banana', 'Cherry'])
print("Array: ",arr)
print("Data Type in Array: ")
print(arr.dtype)

#Define the Data Type in Array
arr = np.array([1,2,3,4], dtype='S')
print("Array:",arr)
print("define the data type in array:",arr.dtype)

arr = np.array([1,2,3,4], dtype='i4')
print("Array:",arr)
print("define the data type in array:",arr.dtype)

arr = np.array([1, 2, 3])
newarr = arr.astype(bool)
print("Array: ",arr)
print("New Array: ",newarr)
print("data dtype of array: ",arr.dtype)
print("data type of New Array:",newarr.dtype)