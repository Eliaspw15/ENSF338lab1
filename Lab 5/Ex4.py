class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.insert(0, element)  # Insert at the head

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()  # Remove from the tail
        else:
            print("Cannot dequeue from an empty queue")
            return -1

    def is_empty(self):
        return len(self.queue) == 0



# Example usage array:
array_queue = ArrayQueue()
array_queue.enqueue(5)
array_queue.enqueue(3)
array_queue.enqueue(9)

print("ArrayQueue:")
print("Dequeue:", array_queue.dequeue())  # Removes 1 (tail)
print("Dequeue:", array_queue.dequeue())  # Removes 2 (tail)
print("Dequeue:", array_queue.dequeue())  # Removes 3 (tail)
print("Dequeue:", array_queue.dequeue())  # Removes 3 (tail) TEST CASE of empty array
