from digraph import Digraph


class TopologicalOrder:
    """
    Implements topological sorting for a directed acyclic graph (DAG).
    """

    def __init__(self, graph):
        """
        Initializes the TopologicalOrder object and performs DFS to find the topological order.
        
        Args:
            graph (Digraph): The directed acyclic graph to perform topological sorting on.
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
            graph (Digraph): The directed acyclic graph to perform DFS on.
            vertex (int): The current vertex being visited.
        """

        self.marked[vertex] = True
        for adjacent in graph.adjacency_lists[vertex]:
            if not self.marked[adjacent]:
                self._dfs(graph, adjacent)
        self.reverse_postorder.append(vertex)

    def get_order(self):
        """
        Returns the topological order as a string representation.
        
        Returns:
            str: A string representation of the topological order.
        """

        return ' -> '.join(str(vertex) for vertex in reversed(self.reverse_postorder))


def main():
    """
    Main function to read a directed acyclic graph (DAG) from a file and compute its topological order.
    """

    FILE_PATH = "data/digraph5.txt"
    digraph = Digraph.from_file(FILE_PATH)
    dfs = TopologicalOrder(digraph)
    print(f"Topological Order: {dfs.get_order()}")


if __name__ == "__main__":
    main()