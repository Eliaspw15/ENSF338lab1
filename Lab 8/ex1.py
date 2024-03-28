import graphviz
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_node(self,node):
        if node not in self.graph:
            self.graph[node] = [] #creates a new Dictionary item in the dict.
    

    def add_edge(self,node1,node2,weight):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append((node2, weight))
            self.graph[node2].append((node1, weight))
        else:
            print("could not find one of the nodes in the Graph, \n make sure when you add a edge you have the node already")
    def removeNode(self,node):
        if node in self.graph:
            for n,edges in self.graph.items():
                self.graph[n] = [(n2, w) for n2, w in edges if n2 != node]
            del self.graph[node]
        else:
            print(f"Node {node} not found in graph")

    def removeEdge(self,n1,n2):
        if n1 in self.graph and n2 in self.graph:
            self.graph[n1]=[(node, weight) for node, weight in self.graph[n1] if node != n2]
            self.graph[n2] = [(node, weight) for node, weight in self.graph[n2] if node != n1]
        else:
            print("one or both nodes are not in the graph.")


