# ChatGPT Assisted
#1. The processdata function has a time complexity of O(n) in the best case, occurring when all elements are less than or equal to 5,
#  requiring only a single pass through the list. In the worst and average cases, its complexity escalates to O(n^2) due to a nested
#  loop that executes for each element greater than 5, leading to quadratic scaling with the list size. This nested loop structure
#  means the function's performance significantly degrades as the number of elements increases. Despite the linear best-case
#  scenario, the dominant factor affecting the function's efficiency is the quadratic behavior introduced by the inner loop.
#  Therefore, the function is generally considered to have a quadratic time complexity in most practical scenarios.

#2.In the original processdata function, the average, best, and worst case complexities are not the same. The best case complexity
#  is O(n) when no elements are greater than 5, and both the average and worst case complexities are O(n^2) due to the nested loop 
#  that potentially iterates over the entire list for each element greater than 5.

# Modified Code. 
def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            li[i] *= 2





