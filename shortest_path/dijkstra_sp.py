from edge_weighted_digraph import EdgeWeightedDigraph
from utils.index_min_pq import IndexMinPQ


class DijkstraSP:
    """
    Implements Dijkstra's algorithm to find the shortest path in an edge-weighted directed graph.
    """

    def __init__(self, digraph, source):
        """
        Initializes the DijkstraSP object and computes the shortest path from the source vertex.
        
        Args:
            digraph (EdgeWeightedDigraph): The edge-weighted directed graph.
            source (int): The source vertex from which to calculate shortest paths.
        """
        self._edge_to = [None] * digraph.number_of_vertices
        self._dist_to = [float('inf')] * digraph.number_of_vertices
        self._priority_queue = IndexMinPQ(digraph.number_of_vertices)

        self._dist_to[source] = 0.0
        self._priority_queue.insert(source, self._dist_to[source])

        while self._priority_queue:
            vertex = self._priority_queue.del_min()

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

            if self._priority_queue.contains(vertex_w):
                self._priority_queue.decrease_key(vertex_w, self._dist_to[vertex_w])
            else:
                self._priority_queue.insert(vertex_w, self._dist_to[vertex_w])

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
    using Dijkstra's algorithm.
    """

    FILE_PATH = "data/ewd.txt"
    digraph = EdgeWeightedDigraph.from_file(FILE_PATH)
    source = 0
    vertex = 3
    dijkstra = DijkstraSP(digraph, source)
    print(f"Distance from {source} to {vertex}: {dijkstra.dist_to(vertex)}")
    print(f"Shortest path from {source} to {vertex}: {dijkstra.path_to(vertex)}")


if __name__ == "__main__":
    main()