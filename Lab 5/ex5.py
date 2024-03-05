#ChatGPT AI Assisted
#1.
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.size = 0
        self.rear = capacity - 1

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            print("enqueue None")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
        print(f"enqueue {item}")

    def dequeue(self):
        if self.is_empty():
            print("dequeue None")
            return None
        front_item = self.queue[self.front]
        print(f"dequeue {front_item}")
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return front_item

    def peek(self):
        if self.is_empty():
            print("peek None")
            return None
        print(f"peek {self.queue[self.front]}")
        return self.queue[self.front]

#2. 
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class ListCircularQueue:
    def __init__(self):
        self.tail = None
        self.size = 0
        self.capacity = 5  # Example fixed size

    def enqueue(self, item):
        if self.size == self.capacity:
            print("enqueue None")  # Queue is full
            return
        
        new_node = Node(item)
        if self.tail is None:
            self.tail = new_node
            self.tail.next = self.tail  # Point to itself
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
        print(f"enqueue {item}")

    def dequeue(self):
        if self.is_empty():
            print("dequeue None")
            return None
        
        head = self.tail.next
        if self.tail == self.tail.next:
            self.tail = None
        else:
            self.tail.next = head.next
        
        self.size -= 1
        print(f"dequeue {head.value}")
        return head.value

    def peek(self):
        if self.is_empty():
            print("peek None")
            return None
        
        head = self.tail.next
        print(f"peek {head.value}")
        return head.value

    def is_empty(self):
        return self.size == 0

#3. 
#CircularQueue (array)
# Assuming a capacity of 5 for the CircularQueue
myQueue = CircularQueue(5)

# Start testing the operations and expected outputs
print("Starting operations on CircularQueue")
myQueue.enqueue(1)  # Expected Output: enqueue 1
myQueue.enqueue(2)  # Expected Output: enqueue 2
myQueue.enqueue(3)  # Expected Output: enqueue 3
myQueue.enqueue(4)  # Expected Output: enqueue 4
myQueue.enqueue(5)  # Expected Output: enqueue 5
myQueue.enqueue(6)  # Expected Output: enqueue None (since the queue is full)

myQueue.peek()      # Expected Output: peek 1 (front of the queue)
myQueue.dequeue()   # Expected Output: dequeue 1
myQueue.dequeue()   # Expected Output: dequeue 2
myQueue.dequeue()   # Expected Output: dequeue 3

myQueue.enqueue(7)  # Expected Output: enqueue 7
myQueue.enqueue(8)  # Expected Output: enqueue 8
myQueue.peek()      # Expected Output: peek 4

myQueue.dequeue()   # Expected Output: dequeue 4
myQueue.dequeue()   # Expected Output: dequeue 5
myQueue.dequeue()   # Expected Output: dequeue 7
myQueue.dequeue()   # Expected Output: dequeue 8
myQueue.dequeue()   # Expected Output: dequeue None (since the queue is now empty)

myQueue.peek()      # Expected Output: peek None (since the queue is empty)
myQueue.enqueue(9)  # Expected Output: enqueue 9
myQueue.enqueue(10) # Expected Output: enqueue 10
myQueue.peek()      # Expected Output: peek 9

# Test wrapping around the circular buffer
myQueue.enqueue(11) # Expected Output: enqueue 11
myQueue.enqueue(12) # Expected Output: enqueue 12
myQueue.enqueue(13) # Expected Output: enqueue 13
myQueue.enqueue(14) # Expected Output: enqueue None (queue is full)

myQueue.peek()      # Expected Output: peek 9
myQueue.dequeue()   # Expected Output: dequeue 9
myQueue.dequeue()   # Expected Output: dequeue 10
myQueue.enqueue(15) # Expected Output: enqueue 15
myQueue.peek()      # Expected Output: peek 11

# Clearing the queue
myQueue.dequeue()   # Expected Output: dequeue 11
myQueue.dequeue()   # Expected Output: dequeue 12
myQueue.dequeue()   # Expected Output: dequeue 13
myQueue.dequeue()   # Expected Output: dequeue 15
myQueue.dequeue()   # Expected Output: dequeue None (empty queue)
myQueue.peek()      # Expected Output: peek None (empty queue)

print("Operations on CircularQueue completed.")

#For Linked List
# Assuming a fixed size (capacity) of 5 for the ListCircularQueue as defined in your implementation
myListQueue = ListCircularQueue()

# Start testing the operations and expected outputs
print("Starting operations on ListCircularQueue")
myListQueue.enqueue(1)  # Expected Output: enqueue 1
myListQueue.enqueue(2)  # Expected Output: enqueue 2
myListQueue.enqueue(3)  # Expected Output: enqueue 3
myListQueue.enqueue(4)  # Expected Output: enqueue 4
myListQueue.enqueue(5)  # Expected Output: enqueue 5
myListQueue.enqueue(6)  # Expected Output: enqueue None (since the queue is full)

myListQueue.peek()      # Expected Output: peek 1 (front of the queue)
myListQueue.dequeue()   # Expected Output: dequeue 1
myListQueue.dequeue()   # Expected Output: dequeue 2
myListQueue.dequeue()   # Expected Output: dequeue 3

myListQueue.enqueue(7)  # Expected Output: enqueue 7
myListQueue.enqueue(8)  # Expected Output: enqueue 8
myListQueue.peek()      # Expected Output: peek 4

myListQueue.dequeue()   # Expected Output: dequeue 4
myListQueue.dequeue()   # Expected Output: dequeue 5
myListQueue.dequeue()   # Expected Output: dequeue 7
myListQueue.dequeue()   # Expected Output: dequeue 8
myListQueue.dequeue()   # Expected Output: dequeue None (since the queue is now empty)

myListQueue.peek()      # Expected Output: peek None (since the queue is empty)
myListQueue.enqueue(9)  # Expected Output: enqueue 9
myListQueue.enqueue(10) # Expected Output: enqueue 10
myListQueue.peek()      # Expected Output: peek 9

# Test adding more elements to fill the queue again
myListQueue.enqueue(11) # Expected Output: enqueue 11
myListQueue.enqueue(12) # Expected Output: enqueue 12
myListQueue.enqueue(13) # Expected Output: enqueue 13
myListQueue.enqueue(14) # Expected Output: enqueue None (queue is full)

myListQueue.peek()      # Expected Output: peek 9
myListQueue.dequeue()   # Expected Output: dequeue 9
myListQueue.dequeue()   # Expected Output: dequeue 10
myListQueue.enqueue(15) # Expected Output: enqueue 15
myListQueue.peek()      # Expected Output: peek 11

# Clearing the queue
myListQueue.dequeue()   # Expected Output: dequeue 11
myListQueue.dequeue()   # Expected Output: dequeue 12
myListQueue.dequeue()   # Expected Output: dequeue 13
myListQueue.dequeue()   # Expected Output: dequeue 15
myListQueue.dequeue()   # Expected Output: dequeue None (empty queue)
myListQueue.peek()      # Expected Output: peek None (empty queue)

print("Operations on ListCircularQueue completed.")
