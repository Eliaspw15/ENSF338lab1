#bubble sort and quicksort
import random
import timeit
from matplotlib import pyplot as plt
import numpy as np
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1] = temp
    return arr

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)  
        quicksort(arr, pivot_index + 1, high)
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


#generate_arrays function from chat gpt
def generate_arrays(num_arrays=20, min_size=5, max_size=100):
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
#best_case_quicksort from chat gpt
def best_case_array(size):
    arr = list(range(1, size + 1))
    random.shuffle(arr)
    return arr

def generate_best_case_arrays(num_arrays, min_size, max_size):
    best_case_arrays = []
    for _ in range(num_arrays):
        size = random.randint(min_size, max_size)
        best_case_arrays.append(best_case_array(size))
    return best_case_arrays

# Generate 20 arrays of various sizes that represent the best case for quicksort
best_case_arrays_QS = generate_best_case_arrays(20, 5, 100)
random_arrays, sorted_arrays, reverse_sorted_arrays = generate_arrays()

#creating arrays for times
Random_times_Bubble = []
Random_times_QS =[]
sorted_times = []
best_caseQS_times = []
rvs_times = []
worst_caseQS_times = []

#arrays with length of the arrays above for plotting
random_lengths_Bubble = [len(arr) for arr in random_arrays] 
sorted_lengths = [len(arr) for arr in sorted_arrays]
reverse_sorted_lengths = [len(arr) for arr in reverse_sorted_arrays]
best_case_arrays_QS_lengths = [len(arr) for arr in best_case_arrays_QS]

for arr in random_arrays: #times for Avg case for Bs
    time = timeit.timeit(lambda: bubble_sort(arr),number = 1)
    Random_times_Bubble.append(time)
    
for arr in sorted_arrays: #times for best case for bs
    time = timeit.timeit(lambda: bubble_sort(arr),number = 1)
    sorted_times.append(time)

for arr in reverse_sorted_arrays: #times for worst case for bs
    time = timeit.timeit(lambda: bubble_sort(arr),number = 1)
    rvs_times.append(time)
    
for arr in random_arrays: #times for AVG case for QS
    time = timeit.timeit(lambda: quicksort(arr,  0, len(arr) - 1), number=1)
    Random_times_QS.append(time)
    
for arr in sorted_arrays: #times for worst case for qs
    time = timeit.timeit(lambda: quicksort(arr,  0, len(arr) - 1), number=1)
    worst_caseQS_times.append(time)

for arr in best_case_arrays_QS: #times for best case for qs
    time = timeit.timeit(lambda: quicksort(arr,  0, len(arr) - 1), number=1)
    best_caseQS_times.append(time)

for arr in best_case_arrays_QS:
    print(quicksort(arr,0,len(arr)-1)) 

fig, axs = plt.subplots(2, 2, figsize=(15, 10))


axs[0, 0].scatter(random_lengths_Bubble, Random_times_Bubble, color='blue', label='Bubble Sort')
axs[0, 0].scatter(random_lengths_Bubble, Random_times_QS, color='red', label='QS')
axs[0, 0].set_title("Length of arrays (average case) vs Time")
axs[0, 0].set_ylabel("Time")
axs[0, 0].set_xlabel("Length of Array")
axs[0, 0].legend()

axs[0, 1].scatter(sorted_lengths, sorted_times, color='blue', label='Bubble Sort')
axs[0, 1].scatter(best_case_arrays_QS_lengths, best_caseQS_times, color='red', label='QS')
axs[0, 1].set_title("Length of array(best case) vs Time")
axs[0, 1].set_ylabel("Time")
axs[0, 1].set_xlabel("Length of Array")
axs[0, 1].legend()


axs[1, 0].scatter(reverse_sorted_lengths, rvs_times, color='blue', label='Bubble Sort')
axs[1, 0].scatter(sorted_lengths, worst_caseQS_times, color='red', label='QS')
axs[1, 0].set_title("Length of array (worst case) vs Time")
axs[1, 0].set_ylabel("Time")
axs[1, 0].set_xlabel("Length of Array")
axs[1, 0].legend()



plt.tight_layout() 
plt.show()
