# 1. A profiler is a kind of module that provides data that describes the complexity of the program through 
    #descriptions of "how often and how long various parts of the program are executed"

#2. Benchmarking is used to measure the time consumed/usage of perform entire operations, so it may be used 
    #to compare say one version of a function to another version of the same function. Profiling is used to 
    #identify time consumed/usage of individual parts of a function. Thus, it can be used to identify parts of a 
    #function that take the most time. 

import timeit
import pstats
import cProfile
import re

def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    # third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]


test_function()
third_function()

cProfile.run('re.compile("test_function")')         #all i need?
cProfile.run('re.compile("third_function")')        #all i need?

#4. The total execution time would be a sum of the time per call of inidvidual parts of each function as the purpose of
    #of the profiler is to highlight how much time is consumed by distinct components of the function.
    #If one wished to view the execution time plainly, benchmarking using modules like timeit, would be more effective.