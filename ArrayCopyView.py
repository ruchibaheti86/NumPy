import numpy as np

#Copy in Array....does affect the any changes in values of previous array
arr = np.array([25,40,30,45,50])
print("Array:",arr)
newarr = arr.copy()
print("NewArray:",newarr)
arr[4] = 35
print("arr[4]:",arr[4])
print("Array:" ,arr)
print("New Array copy(): ",newarr)
#View command in array....Accepts any changes in old array
arr= np.array([25,40,30,45,50])
print("Array:",arr)
x = arr.view()
print("X Array: ",x)
x[3]= 35
print("x[3]:",x[3])
print("Array: ",arr)
print("New Array after view func: ",x)
#Both Copy and View Function in an Array
arr= np.array([25,40,30,45,50])
print("Array: ",arr)
x = arr.copy()
y = arr.view()
print("Array Y with view func: ",y)
print("Base of Array Y",y.base)
print("Array X with copy():",x)
