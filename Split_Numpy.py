import numpy as np
#spliting array
arr1 = np.array([31,23,43, 25,98,76,45,13,45])
print("Array 1:",arr1)
splitarr = np.array_split(arr1,3)
print("spliting the one array into 3 arrays: ", splitarr)

arr2 = np.array([31,23,43, 25,98,76,3])
print("Array 2:",arr2)
splitarr = np.array_split(arr2,6)
print("spliting the one array into 6 arrays: ", splitarr)

#spliting 2D array:
arr = np.array([[21,41], [51,71], [34, 25], [12,11]])
print("2D Array:", arr)
splitarr = np.array_split(arr, 2)
print("2d Array split into two 2D array:", splitarr)
newarr = np.array_split(arr, 2, axis = 1)
print("newarr", newarr)

#Accessing the array an element after split:
arr1 = np.array([31,23,43, 25,98,76,45,13])
print("Array 1:",arr1)
splitarr = np.array_split(arr1,4)
print("elements after spliting the one array into 4 arrays: ")
print(splitarr[0])
print(splitarr[1])
print(splitarr[2])
print(splitarr[3])

arr = np.array([[31,23,43], [25,98,76],[45,13,45]])
print("Array :",arr)
hsplit_arr = np.hsplit(arr, 3)
print("Stacking with rows of an array:", hsplit_arr)
vsplit_arr = np.vsplit(arr, 3)
print("Stacking with columns of an array:", vsplit_arr)

