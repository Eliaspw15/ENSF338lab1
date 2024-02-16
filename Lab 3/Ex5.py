import time
import random
import matplotlib.pyplot as plt
import numpy as np

#Question 1. ChatGPT Assisted
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr

def binary_search(arr, val, start, end):
    # We need to distingush whether we should insert
    # before or after the left boundary.
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1
    # If the array has just one element.
    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        # Find the position where value should be inserted
        j = binary_search(arr, val, 0, i-1)
        # Move all elements after position to create space
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr

#Question 2. ChatGPT Assisted.
sizes = [100, 200, 500, 1000, 2000]
execution_times = {"Traditional": [], "Binary": []}

for size in sizes:
    arr = [random.randint(0, size) for _ in range(size)]

    start_time = time.time()
    insertion_sort(arr.copy())
    end_time = time.time()
    execution_times["Traditional"].append(end_time - start_time)

    start_time = time.time()
    binary_insertion_sort(arr.copy())
    end_time = time.time()
    execution_times["Binary"].append(end_time - start_time)

# Outputting the formatted results
for size in sizes:
    traditional_time = execution_times["Traditional"][sizes.index(size)]
    binary_time = execution_times["Binary"][sizes.index(size)]
    print(f"Array Size: {size}, Traditional Sort Time: {traditional_time:.5f}s, Binary Sort Time: {binary_time:.5f}s")

#Question 3. ChatGPT Assisted
traditional_times = execution_times["Traditional"]
binary_times = execution_times["Binary"]

smooth_sizes = np.linspace(min(sizes), max(sizes), 300)
traditional_interp = np.interp(smooth_sizes, sizes, traditional_times)
binary_interp = np.interp(smooth_sizes, sizes, binary_times)

plt.figure(figsize=(10, 6))
plt.scatter(sizes, traditional_times, color='red', label='Traditional Insertion Sort')
plt.scatter(sizes, binary_times, color='blue', label='Binary Insertion Sort')
plt.plot(smooth_sizes, traditional_interp, 'r--', alpha=0.7)
plt.plot(smooth_sizes, binary_interp, 'b--', alpha=0.7)

plt.title('Comparison of Traditional vs Binary Insertion Sort Execution Times')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.grid(True)
plt.show()

#Question 4.
# In an experiment comparing traditional and binary insertion sort algorithms, the binary insertion sort demonstrated superior performance, 
# particularly with larger array sizes. This efficiency gain is attributed to the binary insertion sort's use of binary search to find the 
# correct position for each element, significantly reducing the number of comparisons needed during sorting. Although both algorithms inherently 
# operate with � ( � 2 ) O(n 2 ) time complexity due to the element shifts required, the reduction in comparisons makes binary insertion sort 
# faster in practice. This characteristic makes it a preferable choice for datasets where reducing comparison operations can lead to notable 
# improvements in execution time, despite the unchanged overall complexity of quadratic time for worst-case scenarios.