import random

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

    def insert(data, root=None):
        current = root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        newnode = Node(data, parent)    
        if root is None:
            root = newnode
        elif data <= parent.data:
            parent.left = newnode
        else:
            parent.right = newnode

        return newnode

    def search(data, root):
        current = root
        while current is not None:
            if data == current.data:
                return current
            elif data <= current.data:
                current = current.left
            else:
                current = current.right
        return None

sorted_vector = list(range(10000))
unsorted_vector = sorted_vector.random.shuffle

sorted_tree = None
for item in sorted_vector:
    sorted_tree = Node.insert(item, sorted_tree)


unsorted_vector = sorted_vector.copy()
random.shuffle(unsorted_vector)         

unsorted_tree = None
for item in unsorted_vector:
    unsorted_tree = Node.insert(item, unsorted_tree)
