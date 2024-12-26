from edge_weighted_digraph import EdgeWeightedDigraph
from topological_order import TopologicalOrder


class AcyclicSP:
    """
    Implements the shortest path algorithm for edge-weighted directed acyclic graphs (DAGs).
    """

    def __init__(self, digraph, source):
        """
        Initializes the AcyclicSP object and computes the shortest path from the source vertex.
        
        Args:
            digraph (EdgeWeightedDigraph): The edge-weighted directed graph.
            source (int): The source vertex from which to calculate shortest paths.
        """
        self._edge_to = [None] * digraph.number_of_vertices
        self._dist_to = [float('inf')] * digraph.number_of_vertices

        self._dist_to[source] = 0.0
        topological_sort = TopologicalOrder(digraph)
        topological_order = topological_sort.get_order()

        for vertex in topological_order:
            for edge in digraph.adjacents(vertex):
                self._relax(edge)

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

    def dist_to(self, vertex):
        """
        Returns the shortest distance to the given vertex.
        
        Args:
            vertex (int): The target vertex.
        
        Returns:
            float: The shortest distance to the vertex.
        """
        return self._dist_to[vertex]

    def path_to(self, vertex):
        """
        Returns the shortest path to the given vertex.
        
        Args:
            vertex (int): The target vertex.
        
        Returns:
            list: A list of edges representing the shortest path to the vertex.
        """
        path = []
        current_edge = self._edge_to[vertex]

        while current_edge:
            path.append(current_edge)
            current_edge = self._edge_to[current_edge.from_edge()]

        return list(reversed(path))


def main():
    """
    Main function to read an edge-weighted directed graph from a file and compute the shortest path
    for a directed acyclic graph (DAG).
    """

    FILE_PATH = "data/ewd.txt"
    digraph = EdgeWeightedDigraph.from_file(FILE_PATH)
    source = 0
    vertex = 3
    dijkstra = AcyclicSP(digraph, source)
    print(f"Distance from {source} to {vertex}: {dijkstra.dist_to(vertex)}")
    print(f"Shortest path from {source} to {vertex}: {dijkstra.path_to(vertex)}")


if __name__ == "__main__":
    main()