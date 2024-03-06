import random
import timeit
import matplotlib.pyplot as plt

#1
class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Cannot pop from an empty stack")
            return -1

    def is_empty(self):
        return len(self.stack) == 0

#2
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.is_empty():
            popped_data = self.head.data
            self.head = self.head.next
            return popped_data
        else:
            print("Cannot pop from an empty stack")
            return -1

    def is_empty(self):
        return self.head is None

#3 did Ex4 first which made following functions of Ex3 easy to implement
def generate_random_tasks():
    tasks = []
    for _ in range(10000):
        task_type = random.choices(["push", "pop"], weights=[0.7, 0.3])[0]
        tasks.append(task_type)
    return tasks

#4
def measure_performance(stack, tasks):
    for task in tasks:
        if task == "push":
            stack.push(random.randint(1, 100))
        elif task == "pop":
            stack.pop()

#5
def plot_distribution(array_times, linked_list_times):
    plt.hist([array_times, linked_list_times], bins=10, alpha=0.5, label=['Array Stack', 'Linked List Stack'])
    plt.legend(loc='upper right')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Stack Implementation Times')
    plt.show()

# example usage Array
array_stack_test = ArrayStack()

array_stack_test.push(5)
array_stack_test.push(3)
array_stack_test.push(9)

print("Pop:", array_stack_test.pop())  # Removes 9
print("Pop:", array_stack_test.pop())  # Removes 3
print("Pop:", array_stack_test.pop())  # Removes 5
print("Pop:", array_stack_test.pop())  # Attempt to pop from an empty stack

# example usage Linked List
linked_list_stack_test = LinkedListStack()

# Push elements onto the stack
linked_list_stack_test.push(5)
linked_list_stack_test.push(3)
linked_list_stack_test.push(9)

# Pop elements from the stack
print("Pop:", linked_list_stack_test.pop())  # Removes 9
print("Pop:", linked_list_stack_test.pop())  # Removes 3
print("Pop:", linked_list_stack_test.pop())  # Removes 5
print("Pop:", linked_list_stack_test.pop())  # Attempt to pop from an empty stack

#run experiments
array_stack = ArrayStack()
linked_list_stack = LinkedListStack()
tasks = generate_random_tasks()

# Measure performance
array_times = timeit.repeat(lambda: measure_performance(array_stack, tasks), number=1, repeat=100)
linked_list_times = timeit.repeat(lambda: measure_performance(linked_list_stack, tasks), number=1, repeat=100)

# Print average times
print("Array Stack Time (avg):", sum(array_times) / len(array_times))
print("Linked List Stack Time (avg):", sum(linked_list_times) / len(linked_list_times))

# Plot the distribution of times
plot_distribution(array_times, linked_list_times)