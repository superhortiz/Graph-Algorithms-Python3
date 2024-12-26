from flow_edge import FlowEdge
import networkx as nx
import matplotlib.pyplot as plt


class FlowNetwork:
    """
    Represents a flow network using adjacency lists.
    """

    def __init__(self, number_of_vertices):
        """
        Initializes a flow network with the specified number of vertices.
        
        Args:
            number_of_vertices (int): The number of vertices in the network.
        """
        self.number_of_vertices = number_of_vertices
        self.adjacency_lists = {vertex: [] for vertex in range(self.number_of_vertices)}

    def add_edge(self, edge):
        """
        Adds a flow edge to the network.
        
        Args:
            edge (FlowEdge): The edge to be added to the network.
        """
        vertex_v = edge.from_edge()
        vertex_w = edge.to_edge()
        self.adjacency_lists[vertex_v].append(edge)
        self.adjacency_lists[vertex_w].append(edge)

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
        Creates a flow network from a file.
        
        Args:
            file_path (str): The path to the file containing the network data.
        
        Returns:
            FlowNetwork: An instance of the FlowNetwork class.
        """
        with open(file_path, 'r') as file:
            # Read the first two lines
            number_of_vertices = int(file.readline().rstrip())

            # Print the first two lines
            graph = cls(number_of_vertices)

            # Iterate over the rest of the file
            for line in file:
                vertex_v, vertex_w, capacity = line.rstrip().split()
                vertex_v, vertex_w, capacity = int(vertex_v), int(vertex_w), float(capacity)
                edge = FlowEdge(vertex_v, vertex_w, capacity)
                graph.add_edge(edge)

            return graph

    def to_networkx_graph(self):
        """
        Converts the flow network to a NetworkX directed graph.
        
        Returns:
            networkx.DiGraph: A NetworkX directed graph representing the same flow network.
        """
        graph = nx.DiGraph()

        # Add Edges to NetworkX Graph
        for vertex_v in range(self.number_of_vertices):
            for edge in self.adjacency_lists[vertex_v]:
                graph.add_edge(edge.vertex_v, edge.vertex_w, capacity=edge.capacity, flow=edge.flow)
        return graph


def main():
    """
    Main function to read a flow network from a file, convert it to a NetworkX graph,
    and visualize it using Matplotlib.
    """

    FILE_PATH = "data/fn.txt"
    graph = FlowNetwork.from_file(FILE_PATH)

    # Convert to NetworkX graph
    networkx_graph = graph.to_networkx_graph()

    # Position nodes using a layout
    pos = nx.spring_layout(networkx_graph)

    # Draw the nodes and edges
    nx.draw(networkx_graph, pos, with_labels=True)

    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(networkx_graph, 'weight')
    nx.draw_networkx_edge_labels(networkx_graph, pos, edge_labels={(u, v): f"{d['flow']} / {d['capacity']}" for u, v, d in networkx_graph.edges(data=True)})

    plt.show()


if __name__ == "__main__":
    main()