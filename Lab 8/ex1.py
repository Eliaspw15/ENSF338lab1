
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_node(self,node):
        if vertex not in self.graph:
            self.graph[node] = [] #creates a new Dictionary item in the dict.
    

    def add_edge(self,node1,node2,weight):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node1].append(weight)
            self.graph[node2].append(node1)
            self.graph[node2].append(weigth)
        else:
            print("could not find one of the nodes in the Graph, \n make sure when you add a edge you have the node already")
    def removeNode(node):
        if node is in self.graph:
            del self.graph[node]
    def removeEdge(n1,n2):


    
        



