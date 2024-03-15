import sys
#ChatGPT AI Assisted

#Defining Tree Node Class
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

#Parsing an input expression into a tree. 
def parse_expression(expression):
    tokens = expression.split()
    ops_stack = []  # Stack for operators and parentheses
    nodes_stack = []  # Stack for nodes

    for token in tokens:
        if token == '(':
            ops_stack.append(token)
        elif token.isdigit():  # If the token is a number
            nodes_stack.append(Node(int(token)))
        elif token in ['+', '-', '*', '/']:
            while (ops_stack and ops_stack[-1] != '('):
                # Perform reduction if possible
                op = ops_stack.pop()
                right = nodes_stack.pop()
                left = nodes_stack.pop()
                nodes_stack.append(Node(op, None, left, right))
            ops_stack.append(token)  # Push current operator
        elif token == ')':
            # Pop until '(' is encountered
            while ops_stack[-1] != '(':
                op = ops_stack.pop()
                right = nodes_stack.pop()
                left = nodes_stack.pop()
                nodes_stack.append(Node(op, None, left, right))
            ops_stack.pop()  # Remove '('

    # Perform any remaining operations
    while ops_stack:
        op = ops_stack.pop()
        right = nodes_stack.pop()
        left = nodes_stack.pop()
        nodes_stack.append(Node(op, None, left, right))

    return nodes_stack.pop()  # The last item is the root of the tree


#Using post order traversal, compute expressions. 
def compute_post_order(node):
    if node is None:
        return 0
    if isinstance(node.data, int):
        return node.data  # Leaf node, return its value

    left_val = compute_post_order(node.left)
    right_val = compute_post_order(node.right)

    # Apply the operation based on the node's data
    if node.data == '+':
        return left_val + right_val
    elif node.data == '-':
        return left_val - right_val
    elif node.data == '*':
        return left_val * right_val
    elif node.data == '/':
        return left_val / right_val

def main():
    if len(sys.argv) > 1:
        expression = " ".join(sys.argv[1:])
        root = parse_expression(expression)
        result = compute_post_order(root)
        print(result)
    else:
        print("Please provide an arithmetic expression.")

if __name__ == "__main__":
    main()