import random
import time
import matplotlib.pyplot as plt
import numpy as np

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >=left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

def run_quicksort_and_measure_time(size):
    arr = [random.randint(1, 100) for _ in range(size)]
    start_time = time.time()
    quicksort(arr, 0, len(arr) - 1)
    end_time = time.time()
    return end_time - start_time

input_sizes = [16, 32, 64, 128, 256, 512, 1024]
run_times = [run_quicksort_and_measure_time(size) for size in input_sizes]

plt.plot(input_sizes, run_times, marker='o', linestyle='-', color='b', label='Quicksort Runtime')
plt.xlabel('Input Size')
plt.ylabel('Runtime (seconds)')
plt.title('Quicksort Runtime for Increasing Input Sizes')
plt.legend()
plt.show()


        