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
