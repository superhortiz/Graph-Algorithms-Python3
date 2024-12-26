from directed_edge import WeightedEdge
import networkx as nx
import matplotlib.pyplot as plt


class EdgeWeightedDigraph:
    """
    Represents an edge-weighted directed graph using adjacency lists.
    """

    def __init__(self, number_of_vertices):
        """
        Initializes an edge-weighted directed graph with the specified number of vertices.
        
        Args:
            number_of_vertices (int): The number of vertices in the graph.
        """
        self.number_of_vertices = number_of_vertices
        self.adjacency_lists = {vertex: [] for vertex in range(self.number_of_vertices)}
        self.edges = []

    def add_edge(self, edge):
        """
        Adds a weighted edge to the graph.
        
        Args:
            edge (WeightedEdge): The edge to be added to the graph.
        """
        vertex_v = edge.from_edge()
        self.adjacency_lists[vertex_v].append(edge)
        self.edges.append(edge)

    def adjacents(self, vertex_v):
        """
        Returns the edges adjacent to the given vertex.
        
        Args:
            vertex_v (int): The vertex for which adjacent edges are to be returned.
        
        Returns:
            list: A list of edges adjacent to the given vertex.
        """
        return self.adjacency_lists[vertex_v]

    @classmethod
    def from_file(cls, file_path):
        """
        Creates an edge-weighted directed graph from a file.
        
        Args:
            file_path (str): The path to the file containing the graph data.
        
        Returns:
            EdgeWeightedDigraph: An instance of the EdgeWeightedDigraph class.
        """
        with open(file_path, 'r') as file:
            # Read the first two lines
            number_of_vertices = int(file.readline().rstrip())

            # Print the first two lines
            graph = cls(number_of_vertices)

            # Iterate over the rest of the file
            for line in file:
                vertex_v, vertex_w, weight = line.rstrip().split()
                vertex_v, vertex_w, weight = int(vertex_v), int(vertex_w), float(weight)
                edge = WeightedEdge(vertex_v, vertex_w, weight)
                graph.add_edge(edge)

            return graph

    def to_networkx_graph(self):
        """
        Converts the graph to a NetworkX directed graph.
        
        Returns:
            networkx.DiGraph: A NetworkX directed graph representing the same edge-weighted directed graph.
        """
        graph = nx.DiGraph()

        # Add Edges to NetworkX Graph
        for vertex_v in range(self.number_of_vertices):
            for edge in self.adjacency_lists[vertex_v]:
                graph.add_edge(edge.vertex_v, edge.vertex_w, weight=edge.weight)
        return graph


def main():
    """
    Main function to read an edge-weighted directed graph from a file, convert it to a NetworkX graph,
    and visualize it using Matplotlib.
    """

    FILE_PATH = "data/ewd.txt"
    graph = EdgeWeightedDigraph.from_file(FILE_PATH)

    # Convert to NetworkX graph
    networkx_graph = graph.to_networkx_graph()

    # Position nodes using a layout
    pos = nx.spring_layout(networkx_graph)

    # Draw the nodes and edges
    nx.draw(networkx_graph, pos, with_labels=True)

    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(networkx_graph, 'weight')
    nx.draw_networkx_edge_labels(networkx_graph, pos, edge_labels=edge_labels, font_size=12)

    plt.show()


if __name__ == "__main__":
    main()