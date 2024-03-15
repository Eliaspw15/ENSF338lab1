import array
import random 
import timeit
#help from chat gpt
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data < value:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.head is None:
            raise IndexError("Priority queue is empty")
        else:
            value = self.head.data
            self.head = self.head.next
            return value
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

class Heap:
    def __init__(self):
        #array of unsigned ints
        self.heap = array.array('i') 

    def heapify(self, arr):
        self.heap = array.array('i', arr)
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(i)

    def enqueue(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def dequeue(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] <= self.heap[parent_index]:
                break
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index

    def heapify_down(self, index):
        n = len(self.heap)
        while index < n:
            left_child_index = 2 * index +1
            right_child_index = 2 * index +2
            largest = index

            if left_child_index < n and self.heap[left_child_index] > self.heap[largest]:
                largest = left_child_index
            if right_child_index < n and self.heap[right_child_index] > self.heap[largest]:
                largest = right_child_index

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

def gen_tasks():
    tasks =[]
    for x in range(1000):
        if random.random() < 0.7: #generates random flaot b/w 0-1
            tasks.append(('enqueue', random.randint(1,100)))
        else:
            tasks.append(('dequeue',None))

    return tasks

tasks = gen_tasks()
LL = ListPriorityQueue()
heap = Heap()

enqueue_time_LL = timeit.timeit(lambda: [LL.enqueue(value) for task, value in tasks if task == 'enqueue'], number=1)
dequeue_time_LL = timeit.timeit(lambda: [LL.dequeue() for task, x in tasks if task == 'dequeue'],number=1)
enqueue_time_AH = timeit.timeit(lambda: [heap.enqueue(value) for task, value in tasks if task == 'enqueue'], number=1)

dequeue_time_AH = timeit.timeit(lambda: [heap.dequeue() for task, x in tasks if task == 'dequeue'], number=1)

print("Array Heap:")
print("Enqueue time:", enqueue_time_AH)
print("Dequeue time:", dequeue_time_AH)
print("LLPriorityQueue:")
print("Enqueue time:",enqueue_time_LL)
print("Enqueue time:", dequeue_time_LL)
    
#Array Heap is faster. This is due to time complexity of enqueue and dequeue.
#in linked list it has to go through entire list and has a time complexity of O(n)
#where as in Array Heap it has O(logn) time comlexity because insertion is easier in arrays and can restore
# heap propertys by swapping elements with parent.