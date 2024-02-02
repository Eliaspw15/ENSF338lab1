#Used ChatGPT to write fact_list_comprehension() 
import timeit
import math

# Function to calculate factorial using recursion
def fact_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_recursive(n - 1)

# Function to calculate factorial using a for loop
def fact_for_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Function to calculate factorial using list comprehension
def fact_list_comprehension(n):
    return math.prod([i for i in range(1, n + 1)])

# Measure the execution time for 10000 instances of fact(100)
time_recursive = timeit.timeit(lambda: fact_recursive(100), number=10000)
print(f"Execution time for recursive factorial: {time_recursive:.5f} seconds")

time_for_loop = timeit.timeit(lambda: fact_for_loop(100), number=10000)
print(f"Execution time for for loop factorial: {time_for_loop:.5f} seconds")

time_list_comprehension = timeit.timeit(lambda: fact_list_comprehension(100), number=10000)
print(f"Execution time for list comprehension factorial: {time_list_comprehension:.5f} seconds")
