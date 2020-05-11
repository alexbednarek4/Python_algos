# When working with graphs, we must first create the edges between nodes

# Creating graph using an adjacency list
class Graph:
    def __init__(self, Nodes):
        self.nodes = Nodes
        self.adj_list = {}
        # Initialize nodes in adj list and set value as empty list
        for node in self.nodes:
            self.adj_list[node] = []

    def print_adj_list(self):
        for node in self.nodes:
            print(node, "->", self.adj_list[node])
    
    def add_edge(self, u, v):
        self.adj_list[v].append(u)
        self.adj_list[u].append(v)

    def degree(self, node):
        # Degree is total number of edges coming in and out of graph
        degree = len(self.adj_list[node])
        return degree


nodes = ["A", "B", "C", "D", "E"]
newGraph = Graph(nodes)
newGraph.add_edge("A", "B")
newGraph.add_edge("A", "C")
newGraph.add_edge("B", "D")
newGraph.add_edge("C", "D")
newGraph.add_edge("C", "E")
newGraph.add_edge("D", "E")
print(newGraph.adj_list)
print("Degree of C: ", newGraph.degree("C"))