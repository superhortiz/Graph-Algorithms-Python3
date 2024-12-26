from edge_weighted_digraph import EdgeWeightedDigraph


class TopologicalOrder:
    """
    Implements topological sorting for an edge-weighted directed graph.
    """

    def __init__(self, graph):
        """
        Initializes the TopologicalOrder object and performs DFS to find the topological order.
        
        Args:
            graph (EdgeWeightedDigraph): The edge-weighted directed graph to perform topological sorting on.
        """
        self.marked = [False] * graph.number_of_vertices
        self.reverse_postorder = []

        for vertex in range(graph.number_of_vertices):
            if not self.marked[vertex]:
                self._dfs(graph, vertex)

    def _dfs(self, graph, vertex):
        """
        Recursively performs DFS to compute the reverse postorder.
        
        Args:
            graph (EdgeWeightedDigraph): The edge-weighted directed graph to perform DFS on.
            vertex (int): The current vertex being visited.
        """
        self.marked[vertex] = True
        for edge in graph.adjacency_lists[vertex]:
            adjacent = edge.to_edge()
            if not self.marked[adjacent]:
                self._dfs(graph, adjacent)
        self.reverse_postorder.append(vertex)

    def get_order(self):
        """
        Returns the topological order as a reversed list of vertices.
        
        Returns:
            list: A reversed list of vertices in topological order.
        """
        return reversed(self.reverse_postorder)


def main():
    """
    Main function to read an edge-weighted directed graph from a file and compute its topological order.
    """

    FILE_PATH = "data/ewd.txt"
    digraph = EdgeWeightedDigraph.from_file(FILE_PATH)
    top_order = TopologicalOrder(digraph)
    print(f"Topological Order: {list(top_order.get_order())}")


if __name__ == "__main__":
    main()