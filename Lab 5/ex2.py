import random
import timeit
#ChatGPT AI Assisted

#1. Class that sorts after each enqueue
class PriorityQueueSortAfterEnqueue:
    def __init__(self):
        self.array = []

    def enqueue(self, item):
        """Add an item to the queue and sort it."""
        self.array.append(item)
        self.array = self.merge_sort(self.array)

    def dequeue(self):
        """Remove and return the highest priority item."""
        if not self.is_empty():
            return self.array.pop(0)
        else:
            raise IndexError("Dequeue from empty priority queue.")

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.array) == 0

    def merge_sort(self, array):
        """Sort the array using merge sort algorithm."""
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1

        return array

#2. Class that maintains sorted order on each enqueue
class PriorityQueueInsertSorted:
    def __init__(self):
        self.array = []

    def enqueue(self, item):
        """Insert an item into the queue so that the queue remains sorted."""
        # If the array is empty or the item is larger than the last item, append it.
        if self.is_empty() or item >= self.array[-1]:
            self.array.append(item)
        else:
            # Find the correct position for the item so that the array remains sorted
            for i in range(len(self.array)):
                if item < self.array[i]:
                    self.array.insert(i, item)
                    break

    def dequeue(self):
        """Remove and return the highest priority item."""
        if not self.is_empty():
            return self.array.pop(0)
        else:
            raise IndexError("Dequeue from empty priority queue.")

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.array) == 0


#3. Function to generate tasks
def generate_tasks(n=1000):
    """Generate a list of 'n' tasks, each being either 'enqueue' with a probability of 0.7
    or 'dequeue' with a probability of 0.3."""
    tasks = []
    for _ in range(n):
        # Generate a random number between 0 and 1
        task_type = random.random()
        # Append 'enqueue' or 'dequeue' to the tasks list based on the probability
        if task_type <= 0.7:
            tasks.append('enqueue')
        else:
            tasks.append('dequeue')
    return tasks

#4. Function to execute tasks on a given priority queue
def execute_tasks(pq, tasks):
    for task in tasks:
        if task == 'enqueue':
            pq.enqueue(random.randint(1, 100))  # Assuming enqueue tasks need a random integer
        elif task == 'dequeue' and not pq.is_empty():
            pq.dequeue()

# Function to measure and compare performance
def measure_performance():
    setup_code = """
from __main__ import PriorityQueueSortAfterEnqueue, PriorityQueueInsertSorted, generate_tasks, execute_tasks
    """
    test_code_1 = """
tasks = generate_tasks()
pq1 = PriorityQueueSortAfterEnqueue()
execute_tasks(pq1, tasks)
    """
    test_code_2 = """
tasks = generate_tasks()
pq2 = PriorityQueueInsertSorted()
execute_tasks(pq2, tasks)
    """

    # Measure time for PriorityQueueSortAfterEnqueue
    time1 = timeit.timeit(setup=setup_code, stmt=test_code_1, number=100)
    print("Average execution time for PriorityQueueSortAfterEnqueue:", time1 / 100)

    # Measure time for PriorityQueueInsertSorted
    time2 = timeit.timeit(setup=setup_code, stmt=test_code_2, number=100)
    print("Average execution time for PriorityQueueInsertSorted:", time2 / 100)

measure_performance()

#5. The PriorityQueueInsertSorted implementation is faster for large datasets because it avoids the overhead of sorting the entire array
#  after each enqueue operation by inserting elements in their correct position to maintain order. This efficiency comes from reducing
#  the complexity of enqueue operations from O(n log n) to O(n) in the worst case, which is particularly advantageous when dealing with
#  a high volume of enqueue actions. 
