class Graph: 
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2, weight):
        self.graph[node1].append((node2, weight))
        self.graph[node2].append((node1, weight))

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):    #chatgpt assisted
        x_root = self.find_parent(parent, x)
        y_root = self.find_parent(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(self):
        result = Graph()
        parent = {}
        rank = {}
        edges = []

        for node, neighbors in self.graph.items():
            for neighbor, weight in neighbors:
                edges.append((weight, node, neighbor))

        edges.sort() 

        for node in self.graph:
            parent[node] = node
            rank[node] = 0

        # Kruskal's algorithm, chatgpt assisted
        for weight, node1, node2 in edges:
            x = self.find_parent(parent, node1)
            y = self.find_parent(parent, node2)

            if x != y:
                result.add_node(node1)
                result.add_node(node2)
                result.add_edge(node1, node2, weight)
                self.union(parent, rank, x, y)

        return result

#usage:
graph = Graph()
graph.add_node(0)
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_edge(0, 1, 10)
graph.add_edge(0, 2, 6)
graph.add_edge(0, 3, 5)
graph.add_edge(1, 3, 15)
graph.add_edge(2, 3, 4)

mst_graph = graph.kruskal()
print(mst_graph.graph)
