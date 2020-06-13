import numpy as np

#Creation of Zero Dimensional Array
arr_a = np.array([42])
print("Zero Dimensional Array: ", arr_a)

#Creation One Dimensional Array
arr_b = np.array([1,2,3])
print("One Dimensional Array: ", arr_b)

#Creation Two Dimensional Array
arr_c = np.array([[1,2,3], [4,5,6]])
print("Two Dimensional Array: ", arr_c)

#Creation Three-Dimensional Array
arr_d= np.array([[[1,2,3,], [4,5,6]], [[1,2,3,], [4,5,6]]])
print("Three Dimensional Array: ",arr_d)

#Dimensional Command: ndim
print("Dimensions of array:")
print("arr_a:",arr_a.ndim, "\n", "arr_b:",arr_b.ndim,"\n", "arr_c:",arr_c.ndim, "\n", "arr_d",arr_d.ndim)
