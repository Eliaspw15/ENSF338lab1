import random
import timeit
import matplotlib.pyplot as plt

# 1
class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.insert(0, element)  # Insert at the head

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()  # Remove AND return from the tail
        else:
            print("Cannot dequeue from an empty queue")
            return -1

    def is_empty(self):
        return len(self.queue) == 0

# 2
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, element):
        new_node = Node(element)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):      #chatgpt assisted
        if not self.is_empty():
            removed_data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return removed_data
        else:
            print("Cannot dequeue from an empty queue")
            return -1

    def is_empty(self):
        return self.head is None

# 3 chatgpt assisted
def generate_random_tasks():
    tasks = []
    for _ in range(10000):
        task_type = random.choices(["enqueue", "dequeue"], weights=[0.7, 0.3])[0]
        tasks.append(task_type)
    return tasks

# 4 chatgpt assisted
def measure_performance(queue, tasks):
    for task in tasks:
        if task == "enqueue":
            queue.enqueue(random.randint(1, 100))
        elif task == "dequeue":
            queue.dequeue()

# 5 chatgpt assisted
def plot_distribution(array_times, linked_list_times):
    plt.hist([array_times, linked_list_times], bins=10, alpha=0.5, label=['Array Queue', 'Linked List Queue'])
    plt.legend(loc='upper right')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Queue Implementation Times')
    plt.show()


# Example usage array:
array_queue = ArrayQueue()
array_queue.enqueue(5)
array_queue.enqueue(3)
array_queue.enqueue(9)

print("Array Queue:")
print("Dequeue:", array_queue.dequeue())  
print("Dequeue:", array_queue.dequeue())  
print("Dequeue:", array_queue.dequeue())  
print("Dequeue:", array_queue.dequeue())  # TEST CASE of attempt to dequeue from empty array

# Example usage Linked List
linked_list_queue = LinkedListQueue()
linked_list_queue.enqueue(5)
linked_list_queue.enqueue(3)
linked_list_queue.enqueue(9)

print("Dequeue:", linked_list_queue.dequeue())  
print("Dequeue:", linked_list_queue.dequeue())  
print("Dequeue:", linked_list_queue.dequeue())  
print("Dequeue:", linked_list_queue.dequeue()) # TEST CASE of attempt to dequeue from empty array

# Run the experiments
array_queue = ArrayQueue()
linked_list_queue = LinkedListQueue()
tasks = generate_random_tasks()

array_times = timeit.repeat(lambda: measure_performance(array_queue, tasks), number=1, repeat=100)
linked_list_times = timeit.repeat(lambda: measure_performance(linked_list_queue, tasks), number=1, repeat=100)

#print("Array Queue Time (avg):", sum(array_times) / len(array_times))
#print("Linked List Queue Time (avg):", sum(linked_list_times) / len(linked_list_times))

# Plot the distribution of times
plot_distribution(array_times, linked_list_times)
