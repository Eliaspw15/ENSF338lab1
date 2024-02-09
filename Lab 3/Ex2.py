#bubble sort and quicksort
import random
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

import random
import timeit

def generate_random_arrays(num_arrays, max_size, max_value):
    random_arrays = []
    for _ in range(num_arrays):
        array_size = random.randint(1, max_size)
        random_array = [random.randint(1, max_value) for _ in range(array_size)]
        random_arrays.append(random_array)
    return random_arrays

# generates 20 random arrays with various sizes:
random_arrays = generate_random_arrays(num_arrays=20, max_size=150, max_value=1000)

arrays_length = []
elapsed_time = []

for i in range(len(random_arrays)):
    arrays_length.append(len(random_arrays[i]))
    print(f"Array {i} Length is: {arrays_length[i]}\n")

for i in range(len(random_arrays)):
    random_arrays[i] = bubble_sort(random_arrays[i])

for i in range(len(random_arrays)):
    print(f"Array {i}: {random_arrays[i]}\n\n")


