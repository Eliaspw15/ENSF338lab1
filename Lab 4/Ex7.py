import time
import matplotlib.pyplot as plt

class Node: #chatgpt assistance used to generate the given methods as comparing the two functions requires the "unoptimized" function to be able to access these methods
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None #single linked list, no tail pointer

    def insert_head(self, node):
        node.next = self.head
        self.head = node

    def insert_tail(self, node):
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def get_size(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size

    def get_element_at_position(self, pos):
        current = self.head
        for _ in range(pos):
            if current is None:
                return None
            current = current.next
        return current

    def reverse(self):
        new_head = None
        prev_node = None
        for i in range(self.get_size()-1, -1, -1):
            current_node = self.get_element_at_position(i)
            current_new_node = Node(current_node.data)
            if new_head is None:
                new_head = current_new_node
            else:
                prev_node.next = current_new_node
            prev_node = current_new_node
        self.head = new_head

#2
    def reverse_optimized(self): #chat gpt assistance used to figure out how to simplify implementation of reverse, my attempts were to try and utilize insert_head/tail, as I assumed they were included for a reason but i couldn't discern how i would without making it more complex than the given implementation
        if self.head is None or self.head.next is None:
            return

        prev_node = None
        current_node = self.head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node

# Function to create a linked list of specified size with random data
def create_linked_list(size):
    linked_list = LinkedList()
    for i in range(size):
        linked_list.insert_tail(Node(data=i))
    return linked_list

# Example usage:
linked_list = create_linked_list(5)
print("Original Linked List:")
current = linked_list.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

#check optimization still functions correctly
linked_list.reverse_optimized()
print("\nLinked List After Optimized Reverse:")
current = linked_list.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")


#3
given_times = []
for size in [1000, 2000, 3000, 4000]:
    linked_list = create_linked_list(size)
    start_time = time.time()
    linked_list.reverse()
    given_times.append(time.time() - start_time)

# Measure time for the optimized implementation
optimized_times = []
for size in [1000, 2000, 3000, 4000]:
    linked_list = create_linked_list(size)
    start_time = time.time()
    linked_list.reverse_optimized()
    optimized_times.append(time.time() - start_time)


# 4
sizes = [1000, 2000, 3000, 4000]
plt.plot(sizes, given_times, label='Given Implementation')
plt.plot(sizes, optimized_times, label='Optimized Implementation')
plt.xlabel('List Size')
plt.ylabel('Time (seconds)')
plt.title('Comparison of Reverse Methods')
plt.legend()
plt.show()