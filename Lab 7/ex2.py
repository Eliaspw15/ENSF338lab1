import timeit
import random
import matplotlib.pyplot as plt

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
        pivot = None
        while True:
            if data <= current.data:
                if current.left is None:
                    current.left = Node(data, parent=current)
                    pivot = current
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(data, parent=current)
                    pivot = current
                    break
                current = current.right

        if pivot is None:
            print("Case #1: Pivot not detected")
            self.update_balances(self.root)  # Update balances from the root
        elif self.height(pivot.left) > self.height(pivot.right) + 1 or self.height(pivot.right) > self.height(pivot.left) + 1:
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            self.update_balances(pivot)  # Update balances from the pivot
        else:
            print("Case 3 not supported")

        return current
    
    def height(self, node):
        if node is None:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1



# Test cases
bst = BST()
print("Test Case 1:")
bst.insert(5)
bst.insert(3)
bst.insert(7)

print("\nTest Case 2:")
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)

print("\nTest Case 3:")
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(6)

print("\nTest Case 4:")
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(6)
bst.insert(8)
