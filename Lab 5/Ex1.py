#creating stack class
import sys
class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("CANNOT POP FROM EMPTY STACK")
        else:
            return self.items.pop()
        
    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            print("LIST IS EMPTY")
        else:
            return self.items[-1]
    
    def size(self):
        return len(self.items)

#function for evaluating the expression
def expression(expr):
    stack = Stack()

    for char in expr:
        if char.isdigit():
            stack.push(int(char))
        elif char in "+/*-":
            stack.push(char)
        elif char == ')':

            num2 = stack.pop()
            num1 = stack.pop()
            op = stack.pop()
            if op == '+':
                answer = num1 + num2
            elif op == '/':
                if num2 == 0:
                    print("Cannot divide by zero")
                    return None
                answer = num1 // num2
            elif op == '-':
                answer = num1 - num2
            elif op == '*':
                answer = num1 * num2
            
            stack.push(answer)
    return stack.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py 'expression'")
        sys.exit(1)
    
    expression_str = sys.argv[1]
    result = expression(expression_str)
    if result is not None:
        print(expression_str, "=", result)