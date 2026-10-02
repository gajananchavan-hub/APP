import numpy as np

# 1-D Array form 1 to 10
arr = np.arange(1,11)
print("Original Array:",  arr)

#slicing operations
print("First 5 elements:",arr[:5])
print("Last 5 elements:",arr[5:])
print("Elements from index 2 to 6:",arr[2:7])


#Statistical  measures
print("sum", np.sum(arr))
print("Mean", np.mean(arr))
print("Minimum", np.min(arr))
print("Maximum", np.max(arr))

# Broadcasting : add 5 to every element
arr = arr + 5
print("After Broadcasting (+5)", arr)
