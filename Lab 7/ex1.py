class Node:
    def __init__(self,data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right= right

    def insert(data, root=None):
        current = root
        parent= None

        While current is not None:
            parent = current
            if Data <= current.data:
                current = current.left_child_index
            else:
                current = current.right_child_index
        newnode = Node(data,parent)        
        if root is None:
            root = newnode
        elif data <= parent.data:
            parent.left = newnode
        else:
            parent.right = newnode
        return newnode

    def search(data,root:
        current = root
        while current is not None:
            if data == current.data:
                return current

            elif data <= current.data:
                current = current.left 
            else:
                current = current.right
        return None
        
        