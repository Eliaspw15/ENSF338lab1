import numpy as np
import time
import matplotlib.pyplot as plt


#3. 
#Inifficient Code. 
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target
    return -1  # Return -1 if the target is not found

#Efficient Code.
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid  # Return the index of the target
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Return -1 if the target is not found

#4. The worst-case complexity of linear search is O(n), and for binary search, it is O(log n).

#5. 
# Generate a sorted array of 1000 elements
arr = np.sort(np.random.randint(0, 100000, 1000))

# Targets for the worst-case scenario
target_linear = arr[-1]  # Last element for linear search
target_binary = 100001   # Value not in the array for binary search

# Measurements
measurements = 100

# Measure execution time for linear search (worst case)
linear_search_times_worst = []
for _ in range(measurements):
    start = time.time()
    linear_search(arr, target_linear)
    end = time.time()
    linear_search_times_worst.append(end - start)

# Measure execution time for binary search (worst case)
binary_search_times_worst = []
for _ in range(measurements):
    start = time.time()
    binary_search(arr, target_binary)
    end = time.time()
    binary_search_times_worst.append(end - start)

# Plotting
plt.figure(figsize=(12, 6))
plt.hist(linear_search_times_worst, alpha=0.5, label='Linear Search (Worst Case)')
plt.hist(binary_search_times_worst, alpha=0.5, label='Binary Search (Worst Case)')
plt.legend()
plt.xlabel('Execution Time (seconds)')
plt.ylabel('Frequency')
plt.title('Execution Times Distribution: Linear vs Binary Search (Worst Case)')
plt.show()
