import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    """Represents an undirected graph using adjacency lists."""

    def __init__(self, number_of_vertices):
        """
        Initializes the graph with the given number of vertices.
        
        Args:
            number_of_vertices (int): The number of vertices in the graph.
        """
        
        self.number_of_vertices = number_of_vertices
        self.adjacency_lists = {vertex: set() for vertex in range(self.number_of_vertices)}

    @property
    def number_of_edges(self):
        """
        Returns the number of edges in the graph.
        
        Returns:
            int: The total number of edges.
        """

        return sum([len(adjacency_list) for adjacency_list in self.adjacency_lists.values()]) // 2

    def add_edge(self, vertex_v, vertex_w):
        """
        Adds an edge between the specified vertices.
        
        Args:
            vertex_v (int): The first vertex.
            vertex_w (int): The second vertex.
        """

        self.adjacency_lists[vertex_v].add(vertex_w)
        self.adjacency_lists[vertex_w].add(vertex_v)

    def remove_edge(self, vertex_v, vertex_w):
        """
        Removes the edge between the specified vertices.
        
        Args:
            vertex_v (int): The first vertex.
            vertex_w (int): The second vertex.
        """

        self.adjacency_lists[vertex_v].remove(vertex_w)
        self.adjacency_lists[vertex_w].remove(vertex_v)

    def adjacents(self, vertex_v):
        """
        Returns the vertices adjacent to the specified vertex.
        
        Args:
            vertex_v (int): The vertex.
        
        Returns:
            set: A set of adjacent vertices.
        """

        return self.adjacency_lists[vertex_v]

    def degree(self, vertex_v):
        """
        Returns the degree of the specified vertex.
        
        Args:
            vertex_v (int): The vertex.
        
        Returns:
            int: The degree of the vertex.
        """

        return len(self.adjacency_lists[vertex_v])

    def max_degree(self):
        """
        Returns the maximum degree of any vertex in the graph.
        
        Returns:
            int: The maximum degree.
        """

        return max([len(adjacency_list) for adjacency_list in self.adjacency_lists.values()])

    def average_degree(self):
        """
        Returns the average degree of the vertices in the graph.
        
        Returns:
            float: The average degree.
        """

        return 2. * self.number_of_edges / self.number_of_vertices

    def number_self_loops(self):
        """
        Returns the number of self-loops in the graph.
        
        Returns:
            int: The number of self-loops.
        """

        count = 0
        for vertex_v in self.adjacency_lists.keys():
            for vertex_w in self.adjacency_lists[vertex_v]:
                if vertex_v == vertex_w:
                    count += 1
        return count // 2

    @classmethod
    def from_file(cls, file_path):
        """
        Creates a graph instance from a file (Alternative constructor).
        
        Args:
            file_path (str): The path to the file containing the graph data.
        
        Returns:
            Graph: An instance of the Graph class.
        """

        with open(file_path, 'r') as file:
            # Read the first two lines
            number_of_vertices = int(file.readline().rstrip())

            # Print the first two lines
            graph = cls(number_of_vertices)

            # Iterate over the rest of the file
            for line in file:
                vertex_v, vertex_w = map(int, line.rstrip().split())
                graph.add_edge(vertex_v, vertex_w)

            return graph

    def to_networkx_graph(self):
        """
        Converts the graph to a NetworkX graph.
        
        Returns:
            networkx.Graph: A NetworkX graph representing the same graph.
        """

        # Create an empty undirected graph using NetworkX
        graph = nx.Graph()

        # Add Edges to NetworkX Graph
        for vertex_v in range(self.number_of_vertices):
            for vertex_w in self.adjacency_lists[vertex_v]:
                graph.add_edge(vertex_v, vertex_w)
        return graph


def main():
    """
    Main function to read a graph from a file, convert it to a NetworkX graph,
    and visualize it using Matplotlib.
    """

    FILE_PATH = "data/graph_test.txt"
    graph = Graph.from_file(FILE_PATH)

    # Convert to NetworkX graph
    networkx_graph = graph.to_networkx_graph()

    # Draw the graph
    nx.draw(networkx_graph, with_labels=True)
    plt.show()


if __name__ == "__main__":
    main()