import random
import timeit
import sys
sys.setrecursionlimit(10**6)

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


def measure_search_performance(tree, elements):
    avg_time = timeit.timeit(lambda: [tree.search(element) for element in elements], number=10) / 10
    total_time = avg_time * len(elements)
    return avg_time, total_time

#2 
sorted_vector = list(range(10000))

bst = Node()
for item in sorted_vector:
    bst.insert(item)

def measure_search_performance(tree, elements):
    avg_time = timeit.timeit(lambda: [tree.search(element) for element in elements], number=10) / 10    #ChatGPT assisted
    total_time = avg_time * len(elements)
    return avg_time, total_time

sorted_avg_time, sorted_total_time = measure_search_performance(bst, sorted_vector)
print("Sorted Tree Search Performance:")
print("Average Time per Search:", sorted_avg_time)
print("Total Time for All Searches:", sorted_total_time)

#3
unsorted_vector = sorted_vector.copy()
random.shuffle(unsorted_vector)

bstUnsorted = Node()
for item in sorted_vector:
    bstUnsorted.insert(item)

unsorted_avg_time, unsorted_total_time = measure_search_performance(bstUnsorted, unsorted_vector)
print("\nUnsorted Tree Search Performance:")
print("Average Time per Search:", unsorted_avg_time)
print("Total Time for All Searches:", unsorted_total_time)

#4  The average search time for a unsorted vector is expected to be lower than the average search time for an sorted vector.
#   This is because a binary search tree built from an unsorted vector is more likely to be balanced as its random
#   building process would result in more parent nodes having a child node that is less than itself (left) AND a child node
#   greater than itself (right). However, with a sorted vector, every child appended it guaranteed to be greater than its parent
#   ultimately degrading the binary search tree into a linked list. Moreover, searching a balanced binary search tree has complexity
#   O(log n) as the search parameter is halved each iteration while a binary search tree degraded into a linked list has complexity
#   O(n) as each "child" would be searched sequentially like elements of a linked list.
