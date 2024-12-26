from edge_weighted_digraph import EdgeWeightedDigraph


class BellmanFord:
    """
    Implements the Bellman-Ford algorithm to find the shortest path in an edge-weighted directed graph
    and to detect negative weight cycles.
    """

    def __init__(self, digraph, source):
        """
        Initializes the BellmanFord object and computes the shortest path from the source vertex.
        
        Args:
            digraph (EdgeWeightedDigraph): The edge-weighted directed graph.
            source (int): The source vertex from which to calculate shortest paths.
        """
        self._edge_to = [None] * digraph.number_of_vertices
        self._dist_to = [float('inf')] * digraph.number_of_vertices
        self._has_negative_cycle = False

        self._dist_to[source] = 0.0

        for _ in range(digraph.number_of_vertices):
            for vertex in range(digraph.number_of_vertices):
                for edge in digraph.adjacents(vertex):
                    self._relax(edge)

        # Check for negative weight cycles
        self._detect_negative_cycle(digraph)

    @property
    def has_negative_cycle(self):
        """
        Checks if the graph has a negative weight cycle.
        
        Returns:
            bool: True if the graph has a negative weight cycle, False otherwise.
        """
        return self._has_negative_cycle
    

    def _relax(self, edge):
        """
        Relaxes the edge and updates the shortest path tree if a shorter path is found.
        
        Args:
            edge (WeightedEdge): The edge to be relaxed.
        """
        vertex_v = edge.from_edge()
        vertex_w = edge.to_edge()
        if self._dist_to[vertex_w] > edge.weight + self._dist_to[vertex_v]:
            self._dist_to[vertex_w] = edge.weight + self._dist_to[vertex_v]
            self._edge_to[vertex_w] = edge

    def _detect_negative_cycle(self, digraph):
        """
        Detects if the graph contains a negative weight cycle.
        
        Args:
            digraph (EdgeWeightedDigraph): The edge-weighted directed graph to check for negative cycles.
        """

        # If there is any edge that needs to be relaxed, then there is a negative cycle
        for vertex in range(digraph.number_of_vertices):
            for edge in digraph.adjacents(vertex):
                vertex_v = edge.from_edge()
                vertex_w = edge.to_edge()
                if self._dist_to[vertex_w] > edge.weight + self._dist_to[vertex_v]:
                    self._has_negative_cycle = True
                    return

    def dist_to(self, vertex):
        """
        Returns the shortest distance to the given vertex.
        
        Args:
            vertex (int): The target vertex.
        
        Returns:
            float: The shortest distance to the vertex if no negative cycle exists, None otherwise.
        """
        if not self.has_negative_cycle:
            return self._dist_to[vertex]
        else:
            return None

    def has_path_to(self, vertex):
        """
        Checks if there is a path to the given vertex.
        
        Args:
            vertex (int): The target vertex.
        
        Returns:
            bool: True if there is a path to the vertex, False otherwise.
        """
        return self._dist_to[vertex] < float('inf')

    def path_to(self, vertex):
        """
        Returns the shortest path to the given vertex.
        
        Args:
            vertex (int): The target vertex.
        
        Returns:
            list: A list of edges representing the shortest path to the vertex if no negative cycle exists, None otherwise.
        """
        if not self.has_negative_cycle:
            path = []
            current_edge = self._edge_to[vertex]

            while current_edge:
                path.append(current_edge)
                current_edge = self._edge_to[current_edge.from_edge()]

            return list(reversed(path))

        else:
            return None


def main():
    """
    Main function to read an edge-weighted directed graph from a file and compute the shortest path
    using the Bellman-Ford algorithm.
    """
    FILE_PATH = "data/ewd.txt"
    digraph = EdgeWeightedDigraph.from_file(FILE_PATH)
    source = 0
    vertex = 3
    bellman_ford = BellmanFord(digraph, source)
    print(f"Does {source} have path to {vertex}? {bellman_ford.has_path_to(vertex)}")
    print(f"Does it have a negative cycle? {bellman_ford.has_negative_cycle}")
    print(f"Distance from {source} to {vertex}: {bellman_ford.dist_to(vertex)}")
    print(f"Shortest path from {source} to {vertex}: {bellman_ford.path_to(vertex)}")


if __name__ == "__main__":
    main()