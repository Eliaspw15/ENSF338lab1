import time
import random
import matplotlib.pyplot as plt
import numpy as np

# Link list node 
class Node: 
    
    def __init__(self, data): 
        self.data = data 
        self.next = None
        self.prev = None
        
def newNode(x):

    temp = Node(0)
    temp.data = x
    temp.next = None
    return temp

# function to find out middle element
def middle(start, last):

    if (start == None):
        return None

    slow = start
    fast = start.next

    while (fast != last):
    
        fast = fast.next
        if (fast != last):
        
            slow = slow.next
            fast = fast.next
        
    return slow

def binarySearch(head,value):
    start = head
    last = None

    while True :
        mid = middle(start, last)

        # If middle is empty
        if (mid == None):
            return None

        # If value is present at middle
        if (mid.data == value):
            return mid

        elif (mid.data < value):
            start = mid.next

        else:
            last = mid

        if not (last == None or last != start):
            break

    # value not present
    return None

class IntegerArray:         
    def __init__(self):     #chapgpt used for assistance with implementation such as how to initiate array
        self.array = []

    def insert(self, value):
        self.array.append(value)

    def binary_search(self, target):
        low, high = 0, len(self.array) - 1

        while low <= high:
            mid = (low + high) // 2
            mid_value = self.array[mid]

            if mid_value == target:
                return mid  # Found the target at index mid
            elif mid_value < target:
                low = mid + 1  # Search in the right half
            else:
                high = mid - 1  # Search in the left half

        return -1  # Target not found
        
    
    
# Driver Code

head = newNode(1)
head.next = newNode(4)
head.next.next = newNode(7)
head.next.next.next = newNode(8)
head.next.next.next.next = newNode(9)
head.next.next.next.next.next = newNode(10)
value = 7
if (binarySearch(head, value) == None):
    print("Value not present\n")
else:
    print("Present")

integer_array = IntegerArray()

for num in [2, 5, 8, 12, 16, 23, 38, 42]:
    integer_array.insert(num)
    
index = integer_array.binary_search(38)

if index != -1:
    print(f'Target {2} found at index {index}')
else:
    print(f'Target {2} not found in the array')
    
#4. Looking at the code for implementation of binary search on a linked list, it becomes clear that it has a time complexity of 
    #O(log n). This can be determined by understanding that it contains a while loop which is called until either a the target 
    #value is found/determined to be absent from linked list. Moreover, within this while loop, the length of the linked list is halved 
    #in every iteration, thus, significantly reducing the time complexity compared to a linear search in which every iteration searches
    #an individual element (resulting in complexity O(n)).
    
#5
sizes = [1000, 2000, 4000, 8000]
execution_times_linked_list = []
execution_times_array = []

for size in sizes:
    LL_binary_search_times = []
    array_binary_search_times = []

    for _ in range(100):  # Repeat 100 times for averaging
        # Create random input lists
        linked_list = [random.randint(0, size) for _ in range(size)]
        #choose random element to use as search target, potential conflict array element not being present in linked list 
        #then creating too many accidental worst case complexity scenarios BUT its all random so logically, the 
        #frequency of worst case complexity scenarios should be the same
        
        integer_array = IntegerArray()
        arr = [random.randint(0, size) for _ in range(size)]
        for num in arr:
            integer_array.insert(num)
        #choose random element to use as search target
        to_search_element = arr[random.randint(0, size-1)]  #choose random element to search for (average case is random element)
        
        start_node = newNode(random.randint(0, size))  # Create the first node with a random integer, CHATGPT assisted to initialize and loop through
        current_node = start_node
        for _ in range(size - 1):  # Repeat to create a linked list of length size
            current_node.next = newNode(random.randint(0, size))
            current_node.next.prev = current_node
            current_node = current_node.next

        # Measure linked list binary search
        start_time = time.time()
        binarySearch(start_node, random.choice(linked_list))
        LL_binary_search_times.append(time.time() - start_time)

        # Measure array binary search
        start_time = time.time()
        integer_array.binary_search(to_search_element)
        array_binary_search_times.append(time.time() - start_time)

    # Calculate average times and append to execution_times
    execution_times_linked_list.append(np.mean(LL_binary_search_times))
    execution_times_array.append(np.mean(array_binary_search_times))

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(sizes, execution_times_linked_list, label='Linked List Binary Search')
plt.plot(sizes, execution_times_array, label='Array Binary Search')
plt.xlabel('Input Size')
plt.ylabel('Average Execution Time (seconds)')
plt.title('Average-case Performance of Binary Search')
plt.legend()
plt.show()