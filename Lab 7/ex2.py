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

    def insert(self, data):     #chatgpt assisted to extend from exercise 1 so that the cases are identified appropiately
        if self.root is None:
            self.root = Node(data)
            print("Case #1: Pivot not detected")
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

        self.update_balances_from_pivot(pivot)  # Update balances from the pivot node

        return current

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

    def update_balances_from_pivot(self, node):
        while node is not None:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            balance = left_height - right_height

            if abs(balance) > 1:
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
                return

            node = node.parent

        print("Case #3: Not supported")

# Test cases
bst = BST()
print("Test Case 1:")
bst.insert(5)       #invokes case 1


print("\nTest Case 2:")
bst.insert(3)       #invokes case 3 because no imbalance + pivot is present, therefore, neither case 1 or 2 invoked
bst.insert(2)       #invokes case 2

print("\nTest Case 3:")
bst.insert(7)       #invokes case 3, case 1 or 2 not present

print("\nTest Case 4:")     #further insertions invoking case 2 and 3 where case 2 occurs every other insertion due to the tree being imbalanced
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(6)
bst.insert(8)
