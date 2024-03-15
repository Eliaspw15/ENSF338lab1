import random
import timeit
import sys
sys.setrecursionlimit(10**6)

#1
#chatGPT assisted, worked off of implementation shown in class
class Node:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        
    def insert(self, data):
        if self.data is None:  # Check if the node is empty
            self.data = data
            return self

        if data <= self.data:
            if self.left is None:
                self.left = Node(data, parent=self)
                return self.left
            else:
                return self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data, parent=self)
                return self.right
            else:
                return self.right.insert(data)
    
    def search(self, data):
        if self.data == data:
            return self
        elif data < self.data and self.left is not None:
            return self.left.search(data)
        elif data > self.data and self.right is not None:
            return self.right.search(data)
        else:
            return None

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def measure_tree_bs_performance(tree, elements):    #ChatGPT assisted
    avg_time = timeit.timeit(lambda: [tree.search(element) for element in elements], number=10) / 10    #ChatGPT assisted
    total_time = avg_time * len(elements)
    return avg_time, total_time

def measure_array_bs_performance(arr, elements):
    avg_time = timeit.timeit(lambda: [binary_search(arr, element) for element in elements], number=10) / 10
    total_time = avg_time * len(elements)
    return avg_time, total_time

#2
sorted_vector = list(range(10000))
unsorted_vector = sorted_vector.copy()
random.shuffle(unsorted_vector)

bst = Node()
for item in unsorted_vector:
    bst.insert(item)

tree_avg_time, tree_total_time = measure_tree_bs_performance(bst, unsorted_vector)
print("Tree Search Performance:")
print("Average Time per Search:", tree_avg_time)
print("Total Time for All Searches:", tree_total_time)

#3
array_search_avg_time, array_search_total_time = measure_array_bs_performance(sorted_vector, sorted_vector)
print("\nBinary Search Performance:")
print("Average Time per Search:", array_search_avg_time)
print("Total Time for All Searches:", array_search_total_time)

#4
#   Binary Search over a sorted array is expected to be faster than a binary search tree built from an unsorted vector because while they both
#   ATTEMPT to halve the search parameter in each step, the tree is still not guaranteed to be perfectly balanced even with unsorted input. 
#   In the last exercise it was stated that an unsorted input increases the chances of producing a MORE balanced tree, but with 10000 
#   random input it is far from assured to be balanced- while unlikely, it is even possible for the tree to nearly degrade into a linked list
#   if the shuffle still results in a nearly sorted vector. Moreover, the binary search applied on the array guarantees the each subproblem is half
#   the size of the previous subproblem. 