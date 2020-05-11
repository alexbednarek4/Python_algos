# When working with graphs, we must first create the edges between nodes

# Creating graph using an adjacency list
class Graph:
    def __init__(self, graph_dict = None):
        """
        Initializes a graph object
            If no dictionary or none is given, an empty 
            dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def vertices(self):
        # returns vertices of graph
        return list(self.graph_dict.keys())
    
    def edges(self):
        # returns edges of graph
        return self.generate_edges()

    def add_vertex(self, vertex):
        """
        If the vertex being added isn't already in self.graph_dict, a new
        vertex key will be added with an empty list as a value to the dictionary.
        otherwise nothing has to be done
        """
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        """
        assumes that edge is of type tuple, list or set;
        between two vertices can be multiple edges
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = []

    def generate_edges(self):
        edges = []
        # For each node in graph
        for vertex in self.graph_dict:
            # For each neighboring node
            for neighbor in self.graph_dict[vertex]:
                if{neighbor, vertex} not in edges:
                # If edge exists, append
                    edges.append({vertex, neighbor})
        return edges