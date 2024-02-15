#bubble sort and quicksort
import random
import timeit
from matplotlib import pyplot as plt
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1] = temp
    return arr

def quicksort(arr,low,high):
    if low>high:
        pivot_index = partition(arr,low, high)
        quicksort(arr,low,pivot_index)
        quicksort(arr,pivot_index + 1, high)
    return arr
    
def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left<= right and arr[left] <= pivot:
            left = left+1
        while arr[right] >= pivot and right >= left:
                right = right-1
        if right < left:
            done = True
        else:
            arr[left],arr[right] = arr[right],arr[left]
    arr[low],arr[right] = arr[right], arr[low]
    return right

#need 20 random arrays of random sizes
#need 20 sorted arrays of same size as above
#need 20 reverse sorted arrays of same size as above

import numpy as np

def generate_arrays(num_arrays=20, min_size=5, max_size=500):
    arrays = []
    sorted_arrays = []
    reverse_sorted_arrays = []
    
    for _ in range(num_arrays):
        size = np.random.randint(min_size, max_size+1)
        
        # Generate random array
        random_array = np.random.randint(0, 1000, size)
        arrays.append(random_array)
        
        # Sort array
        sorted_array = np.sort(random_array)
        sorted_arrays.append(sorted_array)
        
        # Reverse sort array
        reverse_sorted_array = np.sort(random_array)[::-1]
        reverse_sorted_arrays.append(reverse_sorted_array)
    
    return arrays, sorted_arrays, reverse_sorted_arrays

# Example usage:
random_arrays, sorted_arrays, reverse_sorted_arrays = generate_arrays()

Random_times = []
sorted_times = []
rvs_times = []
random_lengths = [len(arr) for arr in random_arrays]
sorted_lengths = [len(arr) for arr in sorted_arrays]
reverse_sorted_lengths = [len(arr) for arr in reverse_sorted_arrays]

for arr in random_arrays:
    time = timeit.timeit(lambda: bubble_sort(arr),number = 1)
    Random_times.append(time)
    
for arr in sorted_arrays:
    time = timeit.timeit(lambda: bubble_sort(arr),number = 1)
    sorted_times.append(time)

for arr in reverse_sorted_arrays:
    time = timeit.timeit(lambda: bubble_sort(arr),number = 1)
    rvs_times.append(time)
    
plt.figure(figsize=(8, 5))
plt.scatter(random_lengths, Random_times, color='blue', label='Random Arrays')
plt.title("Random Lengths vs Time")
plt.ylabel("Time")
plt.xlabel("Length of Array")
plt.legend()


plt.figure(figsize=(8, 5))
plt.scatter(sorted_lengths, sorted_times, color='red', label='Sorted Arrays')
plt.title("Sorted Lengths vs Time")
plt.ylabel("Time")
plt.xlabel("Length of Array")
plt.legend()


plt.figure(figsize=(8, 5))
plt.scatter(reverse_sorted_lengths, rvs_times, color='green', label='Reverse Sorted Arrays')
plt.title("Reverse Sorted Lengths vs Time")
plt.ylabel("Time")
plt.xlabel("Length of Array")
plt.legend()

plt.show()

