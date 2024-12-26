from graph import *


class BipartiteValidation:
    """
    A class to validate if an undirected graph is bipartite.
    """

    def __init__(self, graph):
        """
        Initializes the BipartiteValidation object and performs DFS to check bipartiteness.
        
        Args:
            graph (Graph): The graph to validate.
        """

        self.marked = [False] * graph.number_of_vertices
        self.color = [-1] * graph.number_of_vertices
        self._bipartite = True
        vertex = 0

        # To remove the early ending just remove the self._bipartite checking
        while vertex < graph.number_of_vertices and self._bipartite:
            if not self.marked[vertex]:
                self._dfs(graph, vertex)
            vertex += 1

    @property
    def bipartite(self):
        """
        Checks if the graph is bipartite.
        
        Returns:
            bool: True if the graph is bipartite, False otherwise.
        """

        return self._bipartite
    

    def _dfs(self, graph, vertex):
        """
        Recursively performs DFS to check the bipartiteness of the graph.
        
        Args:
            graph (Graph): The graph to validate.
            vertex (int): The current vertex being visited.
        """

        self.marked[vertex] = True

        for adjacent in graph.adjacency_lists[vertex]:
            if not self.marked[adjacent]:
                self.color[adjacent] = - self.color[vertex]
                self._dfs(graph, adjacent)

            elif self.color[vertex] * self.color[adjacent] > 0:
                    self._bipartite = False


def main():
    """
    Main function to read a graph from a file and check if it is bipartite.
    """

    FILE_PATH = "data/euler_cycle.txt"
    graph = Graph.from_file(FILE_PATH)
    dfs = BipartiteValidation(graph)
    print(f"Is the graph bipartite? {dfs.bipartite}")


if __name__ == "__main__":
    main()