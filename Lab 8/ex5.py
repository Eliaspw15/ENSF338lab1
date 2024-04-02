#1
#Topological sorting can be implemented using Depth First Search (DFS).
#DFS is effective in implementing topological sorting because topological
#sorting requires visiting nodes in sequential order so that if there is 
#a directed edge between node A and node B, node A should maintain a position
#before node B. Since DFS searches down to a leaf node before, backtracking,
#it can be used effectively for a topological sorting method.

import re
class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2, weight):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append((node2, weight))
        else:
            print("Could not find one of the nodes in the graph. "
                  "Make sure when you add an edge, you have the nodes already.")
    
    #deleted node removal and reading from file for simplicity

#2
    def isdag(self):        #chatgpt assisted
        visited = set()
        stack = set()
        cycle = [False]  

        def dfs(node):
            if node in stack:
                cycle[0] = True
                return
            if node in visited:
                return

            visited.add(node)
            stack.add(node)
            for neighbor, _ in self.graph.get(node, []):
                dfs(neighbor)
            stack.remove(node)

        for node in self.graph:
            if not cycle[0]:
                dfs(node)
            else:
                return False
        return True

#3
    def toposort(self):     #chatgpt assisted in combining the DFS and checking if visited process
        if not self.isdag():
            return None

        visited = set()
        stack = []

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor, _ in self.graph.get(node, []):
                dfs(neighbor)
            stack.append(node)

        for node in self.graph:
            dfs(node)

        return stack[::-1]

#USAGE
# usage dag=true, toposort works
g = Graph()

g.add_node(0)
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)

g.add_edge(5, 0, 1)
g.add_edge(4, 0, 1)
g.add_edge(4, 1, 1)
g.add_edge(5, 2, 1)
g.add_edge(3, 1, 1)
g.add_edge(2, 3, 1)

if g.isdag():
    print("The graph is a DAG.")

    topological_order = g.toposort()
    print("Topological order:", topological_order)
else:
    print("The graph contains cycles. Topological sorting is not possible.")

# usage dag=false, toposort says graph contains cycles
g2 = Graph()

g2.add_node(0)
g2.add_node(1)
g2.add_node(2)
g2.add_node(3)
g2.add_node(4)
g2.add_node(5)

g2.add_edge(5, 0, 1)
g2.add_edge(0, 5, 1)    #added one cycle
g2.add_edge(4, 1, 1)
g2.add_edge(5, 2, 1)
g2.add_edge(3, 1, 1)
g2.add_edge(2, 3, 1)

if g2.isdag():
    print("The graph is a DAG.")

    topological_order = g2.toposort()
    print("Topological order:", topological_order)
else:
    print("The graph contains cycles. Topological sorting is not possible.")
