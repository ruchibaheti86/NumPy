import numpy as np
#Searching the numeric array
arr = np.array([2,4,2,9,2])
print("Array: ",arr)
x = np.where(arr == 2)
print("Searching Array with certain element which gives indexes in result : ",x)
x = np.where(arr%3 == 0)
print("Index of an element in array where is divided by 3: ",x)
x = np. where( arr%2 == 1)
print ("Index of odd element in array: ",x)
aa1 = np.array([12,15,19,32])
print("New Array :", aa1)
x = np.searchsorted(aa1, 15)
print("Binary search in array ",x)
x1 = np.searchsorted(aa1, 15, side='right')
print("Search from right side of array:", x1)
x2 = np.searchsorted(aa1, [10,13,20])
print("sorting multiple values in array: ", x2)

