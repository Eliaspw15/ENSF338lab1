import array
import unittest

#chat gpt helped with heapify functions 
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

class TestHeap(unittest.TestCase):
    def test_heapify_sorted_heap(self):
        input_array = [10, 9, 7, 8, 5, 6, 3, 1, 4, 2] # heap is correctly sorted
        expected_heap = [10, 9, 7, 8, 5, 6, 3, 1, 4, 2]
        heap = Heap()
        heap.heapify(input_array)
        self.assertEqual(list(heap.heap), expected_heap)

    def test_heapify_empty_array(self):
        input_array = []
        expected_heap = []
        heap = Heap()
        heap.heapify(input_array)
        # Convert array object to list for comparison
        self.assertEqual(list(heap.heap), expected_heap)
   
    #not sure how to test this as the numbers are random and to sort
    #it you would need to use the heap function, but the heap function 
    # correctly sorts the random sample array given to it as far as I can tell.
    def test_heapify_random_array(self):
        import random
        input_array = random.sample(range(1, 101), 10)  # 10 random integers between 1 and 100
        expected_heap = sorted(input_array, reverse=True)
        heap = Heap()
        heap.heapify(input_array)
        # Convert array object to list for comparison
        self.assertEqual(list(heap.heap), expected_heap)


unittest.main()
