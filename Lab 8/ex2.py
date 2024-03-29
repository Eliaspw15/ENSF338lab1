import re
import heapq
from timeit import default_timer as timer

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}  # Adjacent vertices and their weights
        self.distance = float('inf')  # Distance from the source

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

class Graph:
    def __init__(self):
        self.vert_dict = {}  # Stores vertices in the graph

    def add_vertex(self, node):
        if node not in self.vert_dict:
            new_vertex = Vertex(node)
            self.vert_dict[node] = new_vertex
            return new_vertex

    def get_vertex(self, n):
        return self.vert_dict.get(n)

    def add_edge(self, frm, to, cost=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def dijkstra(self, start, method='fast'):
        start_vertex = self.get_vertex(start)
        start_vertex.set_distance(0)
        
        if method == 'slow':
            unvisited = list(self.vert_dict.values())
            while unvisited:
                # Extract the vertex with the smallest distance
                uv = min(unvisited, key=lambda x: x.get_distance())
                current = uv
                unvisited.remove(uv)
                for next in current.get_connections():
                    new_dist = current.get_distance() + current.get_weight(next)
                    if new_dist < next.get_distance():
                        next.set_distance(new_dist)
        else:  # Using priority queue for the 'fast' method
            priority_queue = []
            heapq.heappush(priority_queue, (start_vertex.get_distance(), start_vertex))
            while priority_queue:
                current_dist, current_vert = heapq.heappop(priority_queue)
                for next_vert in current_vert.get_connections():
                    new_dist = current_vert.get_distance() + current_vert.get_weight(next_vert)
                    if new_dist < next_vert.get_distance():
                        next_vert.set_distance(new_dist)
                        heapq.heappush(priority_queue, (new_dist, next_vert))

def load_graph_from_dot_file(dot_file_path):
    graph = Graph()
    with open(dot_file_path, 'r') as dot_file:
        dot_content = dot_file.read()

    edges = re.findall(r'(\d+) -- (\d+)\s+\[weight=(\d+)\];', dot_content)
    for edge in edges:
        frm, to, cost = edge
        graph.add_edge(frm, to, int(cost))
    return graph

def measure_performance(graph, method):
    start_times = {}
    for node in graph.get_vertices():
        start = timer()
        graph.dijkstra(node, method=method)
        end = timer()
        start_times[node] = end - start

    avg_time = sum(start_times.values()) / len(start_times)
    max_time = max(start_times.values())
    min_time = min(start_times.values())
    return {'average': avg_time, 'max': max_time, 'min': min_time}

# Example usage
dot_file_path = '/Users/josh.geng/code/ENSF338/ENSF338lab1/Lab 8/random.dot'
graph = load_graph_from_dot_file(dot_file_path)

# Measure performance
performance_slow = measure_performance(graph, method='slow')
performance_fast = measure_performance(graph, method='fast')

print("Performance with slow method:", performance_slow)
print("Performance with fast method:", performance_fast)


#Result Discussion
# Performance with slow method: {'average': 0.09180524414416247, 'max': 0.27025890300001265, 'min': 0.08421349300000713}
# Performance with fast method: {'average': 3.5772243654228677e-06, 'max': 7.020500000010088e-05, 'min': 1.6199999919308539e-06}
# The histograms clearly demonstrate the efficiency improvement gained by using a priority queue (fast method) over a linear search (slow method) in 
# Dijkstra's algorithm. The fast method's execution times are not only substantially lower but also show less variability, suggesting that it performs 
# consistently well regardless of the graph's structure. This efficiency is crucial for large graphs or applications requiring real-time computation 
# of shortest paths.