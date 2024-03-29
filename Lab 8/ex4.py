import re
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

    def import_from_file(self, file): #chatgpt used for properly reading then parsing data
        try:
            with open(file, 'r') as f:
                data = f.read()

            # Parse the data using regular expressions
            pattern = r'(\w+)\s*--\s*(\w+)(?:\s*\[weight=(\d+)\])?;'
            matches = re.findall(pattern, data)

            # Clear existing nodes and edges
            self.graph = {}

            # Add nodes and edges from parsed data
            for match in matches:
                node1, node2, weight = match[0], match[1], int(match[2]) if match[2] else 1
                self.add_node(node1)
                self.add_node(node2)
                self.add_edge(node1, node2, weight)

            return self.graph

        except FileNotFoundError:
            print("File not found.")
            return None
        except Exception as e:
            print("Error occurred while importing from file:", e)
            return None
    
    def display_graph(self):
        for node, edges in self.graph.items():
            print(f"{node} --> {edges}")
    
    def dfs_util(self, node, visited, results):
        visited.add(node)
        results.append(node)
        for neighbor, _ in self.graph[node]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited, results)

    def dfs(self):
        visited = set()
        results = []
        for node in self.graph:
            if node not in visited:
                self.dfs_util(node, visited, results)
        return results




class Graph2:
    def __init__(self, nodes=0):
        self.matrix = [[0] * nodes for _ in range(nodes)]
        self.node_map = {}  # Maps node labels to indices in the matrix
        self.nodes = []  # Keeps track of node labels

    def add_node(self, node):
        if node not in self.node_map:
            self.node_map[node] = len(self.nodes)
            self.nodes.append(node)
            for row in self.matrix:
                row.append(0)
            self.matrix.append([0] * (len(self.matrix) + 1))

    def add_edge(self, node1, node2, weight=1):
        if node1 in self.node_map and node2 in self.node_map:
            idx1, idx2 = self.node_map[node1], self.node_map[node2]
            self.matrix[idx1][idx2] = weight
            self.matrix[idx2][idx1] = weight 
        else:
            print("Error: One or both nodes not found.")
            
    def import_from_file(self, file): #chatgpt used for properly reading then parsing data
        try:
            with open(file, 'r') as f:
                data = f.read()

            # Parse the data using regular expressions
            pattern = r'(\w+)\s*--\s*(\w+)(?:\s*\[weight=(\d+)\])?;'
            matches = re.findall(pattern, data)

            # Clear existing nodes and edges
            self.graph = {}

            # Add nodes and edges from parsed data
            for match in matches:
                node1, node2, weight = match[0], match[1], int(match[2]) if match[2] else 1
                self.add_node(node1)
                self.add_node(node2)
                self.add_edge(node1, node2, weight)
            return self.graph
        except FileNotFoundError:
            print("File not found.")
            return None
        except Exception as e:
            print("Error occurred while importing from file:", e)
            return None

    def display_graph(self):
        for node, edges in self.graph.items():
            print(f"{node} --> {edges}")

    def dfs_util(self, v, visited):
        visited[v] = True
        results = [self.nodes[v]]
        for i, val in enumerate(self.matrix[v]):
            if val and not visited[i]:
                results.extend(self.dfs_util(i, visited))
        return results

    def dfs(self):
        visited = [False] * len(self.nodes)
        results = []
        for i in range(len(self.nodes)):
            if not visited[i]:
                results.extend(self.dfs_util(i, visited))
        return results


graph_list = Graph()
graph_matrix = Graph2()

import timeit


file_path = 'random.dot'  # Provide the correct file path
graph_list.import_from_file(file_path)
graph_matrix.import_from_file(file_path)
def dfs_graph_list():
    return graph_list.dfs()

def dfs_graph_matrix():
    return graph_matrix.dfs()

repetitions = 10

# Measure performance
time_list = []
time_matrix = []
for i in range(repetitions):
   time_list.append(timeit.timeit(dfs_graph_list, number=1))
   time_matrix.append(timeit.timeit(dfs_graph_matrix, number=1))

max_time_list = max(time_list)
max_time_matrix = max(time_matrix)
min_time_list = min(time_list)
min_time_matrix = min(time_matrix)
avg_time_matrix = sum(time_matrix)/repetitions
avg_time_list = sum(time_list)/repetitions

print("Adjacency List:")
print(f"Maximum Time: {max_time_list} seconds")
print(f"Minimum Time: {min_time_list} seconds")
print(f"Average Time: {avg_time_list} seconds")

print("\nAdjacency Matrix:")
print(f"Maximum Time: {max_time_matrix} seconds")
print(f"Minimum Time: {min_time_matrix} seconds")
print(f"Average Time: {avg_time_matrix} seconds")

#the reason that adjacency list is faster is because for each vertex it only
#needs to iterate over the exisiting vertices which get stored in the list as opposed
#to the matrix it has to iterate through every column and row of the matrix.
