import numpy as np

# Create 1-D array from 1 to 10
arr = np.arange(1, 11)
print("Original Array:", arr)

# Slicing operations
print("First 5 elements:", arr[:5])
print("Last 5 elements:", arr[5:])
print("Elements from index 2 to 6:", arr[2:7])
print("Alternate elements:", arr[::2])

# Statistical measures
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Broadcasting
arr = arr + 10
print("After adding 10 using broadcasting:", arr)

arr = arr * 2
print("After multiplying by 2 using broadcasting:", arr)