import time
import matplotlib.pyplot as plt

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2) 

#1. This is the fibonacci sequence for n terms.

#2. Yes this is technically a divide and conquer algorithm as it splits the problem into smaller problems. 
    #It is just innefficient because the "smaller" problems are only slightly smaller than the original. 

#3. This function has a time complexity of O(2^n)

#4. Implement a version of the code which uses memoization to improve performance

def fib_memo(n, memo={}):       # ChatGPT Assisted
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        return memo[n]

#5. This funcition has a time complexity of O(n) because each Fibonacci number is computed only once.

#6. Time the original code and your improved version, for all integers between 0 and 35, and plot the results

original_times = []         # Assisted with ChatGPT
memoized_times = []
for i in range(36):
    start = time.time()
    func(i)
    end = time.time()
    original_times.append(end - start)
    
    start = time.time()
    fib_memo(i)
    end = time.time()
    memoized_times.append(end - start)

# Plotting
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(range(36), original_times, label='Original')
plt.xlabel('Fibonacci Number (n)')
plt.ylabel('Time (seconds)')
plt.title('Performance of Original Fibonacci')
plt.legend()
plt.grid(True)
plt.xlim(0, 35)
plt.ylim(0.0, 3.5)

plt.subplot(1, 2, 2)
plt.plot(range(36), memoized_times, label='Memoized', color='orange')
plt.xlabel('Fibonacci Number (n)')
plt.ylabel('Time (seconds)')
plt.title('Performance of Memoized Fibonacci')
plt.legend()
plt.grid(True)
plt.xlim(0, 35)
plt.ylim(0.0, 3.5)

plt.tight_layout()
plt.show()

