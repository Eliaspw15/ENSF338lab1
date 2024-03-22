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

    def update_balances_from_pivot(self, node):
        while node:
            if abs(self.balance_factor(node)) > 1:
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
                self.rebalance(node)
                return
            node = node.parent
        print("Case #3: Balance maintained after adjustment")

    def rebalance(self, node):
        if self.balance_factor(node) > 1:
            if self.balance_factor(node.left) < 0:
                self._lr_rotate(node)
            else:
                self._right_rotate(node)
        elif self.balance_factor(node) < -1:
            if self.balance_factor(node.right) > 0:
                self._rl_rotate(node)
            else:
                self._left_rotate(node)

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right is not None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        x.right = y
        y.parent = x

    def _lr_rotate(self, node):
        self._left_rotate(node.left)
        self._right_rotate(node)

    def _rl_rotate(self, node):
        self._right_rotate(node.right)
        self._left_rotate(node)

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def print_tree(self, node, depth=0, prefix="Root: "):
        if node is not None:
            self.print_tree(node.right, depth + 1, "R--- ")
            print(' ' * depth * 4 + prefix + str(node.data))
            self.print_tree(node.left, depth + 1, "L--- ")


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

def test_case_3b():
    bst = BST()
    print("\nTest Case LR (Left-Right) Imbalance:")
    bst.insert(30)
    bst.insert(10)
    bst.insert(20)  # Triggers LR rotation
    bst.print_tree(bst.root)

    bst = BST()
    print("\nTest Case RL (Right-Left) Imbalance:")
    bst.insert(30)
    bst.insert(50)
    bst.insert(40)  # Triggers RL rotation
    bst.print_tree(bst.root)

test_case_3b()