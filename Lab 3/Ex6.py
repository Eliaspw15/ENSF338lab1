import time
import random
import matplotlib.pyplot as plt
import numpy as np

#Question 1. ChatGPT Assisted
# Define linear and binary search functions
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

#Question 2 & 3. ChatGPT Assisted
# Define quicksort function
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Measure performance of searches
sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
execution_times = {"Linear": [], "Binary": []}
constant_element = 0  # Element to search for

for size in sizes:
    linear_search_times = []
    binary_search_times = []
    for _ in range(100):  # Repeat 100 times for averaging
        arr = [random.randint(0, size) for _ in range(size)]
        arr.append(constant_element)  # Ensure the element is present
        
        # Measure linear search
        random.shuffle(arr)  # Shuffle for linear search
        start_time = time.time()
        linear_search(arr, constant_element)
        linear_search_times.append(time.time() - start_time)
        
        # Measure binary search (requires sorted array)
        arr.sort()
        start_time = time.time()
        binary_search(arr, constant_element)
        binary_search_times.append(time.time() - start_time)
    
    # Calculate average times and append to execution_times
    execution_times["Linear"].append(np.mean(linear_search_times))
    execution_times["Binary"].append(np.mean(binary_search_times))

#Question 4. ChatGPT Assisted
# Plotting performance of searches
plt.figure(figsize=(10, 6))
plt.plot(sizes, execution_times["Linear"], label='Linear Search', marker='o')
plt.plot(sizes, execution_times["Binary"], label='Binary Search', marker='s')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Linear vs Binary Search Performance')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.grid(True, which="both", ls="--")
plt.show()

#4. The performance disparity between linear and binary search is fundamentally rooted in their respective time 
# complexities and operational prerequisites. Linear search operates with a time complexity of \(O(n)\), methodically 
# examining each element until the target is found, which inherently leads to reduced efficiency as the size of the 
# array increases. On the other hand, binary search necessitates a sorted array but benefits from a much more 
# favorable time complexity of \(O(\log n)\). This logarithmic nature significantly enhances its speed for larger 
# datasets by drastically reducing the number of comparisons required to locate the target. The plotted results from 
# the experiment clearly underscore this distinction, illustrating binary search's superior scalability and efficiency 
# in handling extensive arrays.
# Measure performance of quicksort on sorted vs shuffled arrays
performance_sorted = []
performance_shuffled = []

for size in sizes:
    arr_sorted = list(range(size))  # Already sorted
    arr_shuffled = arr_sorted.copy()
    random.shuffle(arr_shuffled)  # Shuffle

    # Measure on sorted array
    start_time = time.time()
    quicksort(arr_sorted)
    performance_sorted.append(time.time() - start_time)
    
    # Measure on shuffled array
    start_time = time.time()
    quicksort(arr_shuffled)
    performance_shuffled.append(time.time() - start_time)

#Question 5 ChatGPT Assisted
# Plotting performance of quicksort
plt.figure(figsize=(10, 6))
plt.plot(sizes, performance_sorted, label='Quicksort on Sorted Array', marker='o')
plt.plot(sizes, performance_shuffled, label='Quicksort on Shuffled Array', marker='s')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Quicksort Performance: Sorted vs Shuffled Input')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.grid(True, which="both", ls="--")
plt.show()
