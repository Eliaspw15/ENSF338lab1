import timeit
import random
import matplotlib.pyplot as plt

#help from chatgpt implementing performance_balance and implementing iteration through bst
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root

        current = self.root
        while True:
            if data <= current.data:
                if current.left is None:
                    current.left = Node(data, parent=current)
                    return current.left
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(data, parent=current)
                    return current.right
                current = current.right

    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None
    
    def height(self, node):
        if node is None:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1
    
    def balance_factor(self, node):
        if node is None:
            return 0 
        else:
            return self.height(node.left) - self.height(node.right)
    
    def __iter__(self):
        yield from self.inorder(self.root)

    def inorder(self, node):
        if node is not None:
            yield from self.inorder(node.left)
            yield node
            yield from self.inorder(node.right)

def generate_searches():
    ints = list(range(1, 1001))
    search_tasks = []
    for i in range(1000):
        random.shuffle(ints)
        search_tasks.append(ints.copy())
    return search_tasks

def performance_balance(search_tasks):
    avg_performance = []
    largest_balances = []

    for task in search_tasks:
        #creates new BST every iteration.
        bst = BST()
        for integer in task:
            bst.insert(integer)

        # Calculation of average performance
        start_time = timeit.default_timer()
        for integer in task:
            bst.search(integer)
        end_time = timeit.default_timer()
        time_taken = end_time - start_time
        avg_performance.append(time_taken / len(task))

        #calculation of largest balance
        nodes = list(bst)
        largest_balance = max(abs(bst.balance_factor(node)) for node in nodes)
        largest_balances.append(largest_balance)

    return avg_performance, largest_balances


search_tasks = generate_searches()
avg_performance, largest_balances = performance_balance(search_tasks)

print("Average Performance:", sum(avg_performance) / len(avg_performance))
print("Largest Absolute Balance:", max(largest_balances))

plt.scatter(largest_balances, avg_performance, alpha=0.5)
plt.xlabel('Absolute Balance')
plt.ylabel('Search Time (seconds)')
plt.title('Scatterplot of Absolute Balance vs Search Time')
plt.show()
