import numpy as np
#Filter the array
arr = np.array([2,4,2,9,2])
print("Array: ",arr)
x = [False, False, True, False, True]
newarr = arr[x]
print("Filtered new array : ",newarr)

#Filteration of array in for and if command as well.
arr = np.array([100, 110, 120, 150, 180])
filterarr = []
for e in arr:
    if e < 150:
        filterarr.append(True)
    else:
       filterarr.append(False)
newarr = arr[filterarr]
print("Filter Array: ", filterarr)
print("New Array: ", newarr)

