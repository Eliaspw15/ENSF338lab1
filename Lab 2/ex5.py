import timeit
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 1. Implement linear and binary search.
def linear_search(arr, target):     # implement linear search
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):     # implement binary search
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# 2. Measure the performance of each on sorted vectors of 1000, 2000, 4000, 8000, 16000, 32000 elements. In each case, 
#    you must do the following for 1000 times, and compute the average.

def measure_time(search_func, arr_size):        # measure_time created with assistance of ChatGPT
    def wrapper():          # Assistance from ChatGPT
        arr = list(range(arr_size))
        target = random.randint(0, arr_size - 1)
        search_func(arr, target)
    execution_time = timeit.timeit(wrapper, number=1000)
    return execution_time / 1000

# Separate function to measure time with 100 iterations and print results
def measure_time_100(search_func, arr_size):        
    def wrapper():          
        arr = list(range(arr_size))
        target = random.randint(0, arr_size - 1)
        search_func(arr, target)
    execution_time = timeit.timeit(wrapper, number=100)
    return execution_time / 100

# Test different array sizes
arr_sizes = [1000, 2000, 4000, 8000, 16000, 32000]

# Print average search time for linear and binary search for each array size
for size in arr_sizes:
    linear_avg_time = measure_time(linear_search, size)
    binary_avg_time = measure_time(binary_search, size)
    print(f"Array size {size}:")
    print(f"Linear search average time: {linear_avg_time:.6f} seconds")
    print(f"Binary search average time: {binary_avg_time:.6f} seconds")
    print()

# Print average search time for linear and binary search for each array size but for 100 iterations
for size in arr_sizes:
    linear_avg_time = measure_time_100(linear_search, size)
    binary_avg_time = measure_time_100(binary_search, size)
    print(f"Array size {size}:")
    print(f"Linear search average time (100 iterations): {linear_avg_time:.6f} seconds")
    print(f"Binary search average time (100 iterations): {binary_avg_time:.6f} seconds")
    print()

# 3. Each plot should also interpolate the data points with an appropriate function. For example, linear complexity with a linear function, quadratic complexity with a quadratic function, etc.
# Used assistance from ChatGPT for plt functions.

linear_avg_times = []
binary_avg_times = []

for size in arr_sizes:
    linear_avg_time = measure_time(linear_search, size)
    binary_avg_time = measure_time(binary_search, size)
    linear_avg_times.append(linear_avg_time)
    binary_avg_times.append(binary_avg_time)

# Fit functions to the data
def linear_func(x, a, b):
    return a * x + b

def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

popt_linear, _ = curve_fit(linear_func, arr_sizes, linear_avg_times)
popt_quadratic, _ = curve_fit(quadratic_func, arr_sizes, binary_avg_times)

# Plot original data
plt.scatter(arr_sizes, linear_avg_times, label='Linear Search Data')
plt.scatter(arr_sizes, binary_avg_times, label='Binary Search Data')

# Plot interpolated curves
plt.plot(arr_sizes, linear_func(np.array(arr_sizes), *popt_linear), label='Linear Fit')
plt.plot(arr_sizes, quadratic_func(np.array(arr_sizes), *popt_quadratic), label='Quadratic Fit')

plt.xlabel('Array Size')
plt.ylabel('Average Search Time (seconds)')
plt.title('Interpolated Average Search Times')
plt.legend()
plt.grid(True)
plt.show()

#4. Used ChatGPT to help aid in answers.
#Linear Function:
# Type of Function: Linear function.
# Parameters of the Function: The linear function has two parameters: the slope (a) and the y-intercept (b).
# Discussion: The linear function represents the average search time as a linear relationship with the array size. 
# The slope (a) indicates the rate of change of the average search time with respect to the array size, while the y-intercept (b) represents 
# the average search time when the array size is zero. The results are what we would expect for linear search, as the average search time should 
# increase linearly with the array size.

#Quadratic Function:
# Type of Function: Quadratic function.
# Parameters of the Function: The quadratic function has three parameters: the coefficient of the quadratic term (a), the coefficient of the 
# linear term (b), and the constant term (c).
# Discussion: The quadratic function represents the average search time as a quadratic relationship with the array size. The coefficient of the 
# quadratic term (a) indicates the curvature of the parabolic shape of the function, while the coefficient of the linear term (b) affects the slope 
# of the function. The constant term (c) represents the value of the function when the array size is zero. The results are expected for binary search, 
# as its average search time tends to increase quadratically with the array size due to its logarithmic time complexity.
