import random

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

    def is_empty(self):     #this method and its use in dequeue was added after comparing with chatgpt assisted solution
        return len(self.queue) == 0

#2
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
            new_node.next = self.head
            self.head = new_node

    def dequeue(self):
        if not self.is_empty():
            removed_data = self.tail.data
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                current = self.head
                while current.next != self.tail:
                    current = current.next
                current.next = None
                self.tail = current
            return removed_data
        else:
            print("Cannot dequeue from an empty queue")
            return -1

    def is_empty(self):
        return self.head is None

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

linked_list_queue = LinkedListQueue()
linked_list_queue.enqueue(5)
linked_list_queue.enqueue(3)
linked_list_queue.enqueue(9)

print("Dequeue:", linked_list_queue.dequeue())  # Removes 3 (tail)
print("Dequeue:", linked_list_queue.dequeue())  # Removes 2 (tail)
print("Dequeue:", linked_list_queue.dequeue())  # Removes 1 (tail)
print("Dequeue:", linked_list_queue.dequeue())

#3
# could be interrupted by is_empty method

#4, 5
# ez