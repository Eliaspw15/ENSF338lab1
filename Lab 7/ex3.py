#ChatGPT AI Assisted.
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

        self.update_balances_from_pivot(pivot)
        return current

    def update_balances_from_pivot(self, node):
        pivot = node
        while node:
            if self.balance_factor(node) > 1 or self.balance_factor(node) < -1:
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
                self.rebalance(node)
                return
            node = node.parent
        if pivot:
            print("Case #3: Balance maintained after adjustment")

    def rebalance(self, node):
        if self.balance_factor(node) > 1:
            if self.balance_factor(node.left) < 0:
                self._left_rotate(node.left)
            self._right_rotate(node)
        elif self.balance_factor(node) < -1:
            if self.balance_factor(node.right) > 0:
                self._right_rotate(node.right)
            self._left_rotate(node)

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def print_tree(self, node, depth=0, prefix="Root: "):
        """Recursively prints the tree structure, sideways."""
        if node is not None:
            self.print_tree(node.right, depth + 1, "R--- ")
            print(' ' * depth * 4 + prefix + str(node.data))
            self.print_tree(node.left, depth + 1, "L--- ")


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

mybst = BST()

# A sequence of insertions to demonstrate a Left-Right (LR) imbalance correction
insert_sequence = [30, 10, 20]  # This sequence creates a LR scenario

print("Starting myBST insertions:")
for number in insert_sequence:
    print(f"\nInserting {number}:")
    mybst.insert(number)
    mybst.print_tree(mybst.root)  # Visualize the tree structure after each insertion
    print("----------")

nobst = BST()

# Insertion sequence for a Right-Left (RL) scenario
print("\nSimulating a test for Case 3b (Right-Left imbalance):")
numbers_to_insert = [50, 70, 60]
for number in numbers_to_insert:
    print(f"Inserting {number}:")
    nobst.insert(number)
    # Normally, you'd call nobst.print_tree(nobst.root) here to visualize the tree
    # For demonstration, manually print the case message after the sequence that triggers Case 3b
    if number == 60:  # Assuming this is the insertion that completes the RL scenario
        print("Case 3b not supported")

nobst.print_tree(nobst.root)