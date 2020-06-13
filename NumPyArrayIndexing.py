import numpy as np

#Array Indexing
arr_one = np.array([10,15,25,30,5,20])
print("Array:",arr_one)
print("Array Indexing:")
print("arr[0]:",arr_one[0])
print("arr[1]:",arr_one[1])
print("Adding first and third element of array: ",arr_one[0] + arr_one[2])

arr_two= np.array([[5,10,15],[20,25,30]])
print("Array_Two", arr_two)
print("2nd element of 1st dim: ", arr_two[0,1])
print("3rd element on 2nd dim: ", arr_two[1, 2])

#Negative Indexing
print("last element of first dimension", arr_two[0,-1])
