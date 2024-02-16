import random
from matplotlib import pyplot as plt
import numpy as np
def bubble_sort(arr):
    swaps = 0
    comparisons = 0
    n = len(arr)
    for i in range(n): 
        for j in range(0,n-i-1): 
            swaps += 1
            if arr[j] > arr[j+1]:
                comparisons += 1
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1] = temp
    num_swaps.append(swaps)
    num_comparisons.append(comparisons)
    return arr
#generates 100 random arrays for avg case
def generate_random_array(length):
    return [random.randint(0, 100) for i in range(length)]

random_arrays = []
num_swaps = []
num_comparisons = []
array_length = []

for i in range(1, 101):  
    random_arrays.append(generate_random_array(i))

for arr in random_arrays:
    bubble_sort(arr)
    array_length.append(len(arr))

plt.figure(figsize=(10, 6))

# Plot number of comparisons
plt.subplot(2, 1, 1)
plt.plot(array_length, num_comparisons, marker='o', label='Number of Comparisons', color='blue')
plt.xlabel('Array Length')
plt.ylabel('Number of Comparisons')
plt.title('Number of Comparisons vs Array Length')

# Fit and plot interpolating function
p_comp = np.polyfit(array_length, num_comparisons, 2)
x_comp = np.linspace(1, len(array_length), 100)
y_comp = np.polyval(p_comp, x_comp)
plt.plot(x_comp, y_comp, linestyle='--', color='orange', label='Interpolating Function (Comparisons)')
plt.legend()

# Plot number of swaps
plt.subplot(2, 1, 2)
plt.plot(array_length, num_swaps, marker='o', label='Number of Swaps', color='green')
plt.xlabel('Array Length')
plt.ylabel('Number of Swaps')
plt.title('Number of Swaps vs Array Length')

# Fit and plot interpolating function for swaps
p_swaps = np.polyfit(array_length, num_swaps, 2)
x_swaps = np.linspace(1, len(array_length), 100)
y_swaps = np.polyval(p_swaps, x_swaps)
plt.plot(x_swaps, y_swaps, linestyle='--', color='red', label='Interpolating Function (Swaps)')
plt.legend()

plt.tight_layout()
plt.show()
