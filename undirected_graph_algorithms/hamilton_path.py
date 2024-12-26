from graph import *


class HamiltonPath:
    """
    Finds Hamiltonian paths in a given graph.
    """

    def __init__(self, graph):
        """
        Initializes the HamiltonPath object and finds Hamiltonian paths.
        
        Args:
            graph (Graph): The graph to find Hamiltonian paths in.
        """
        self.marked = [False] * graph.number_of_vertices
        self.count = 0

        for vertex in range(graph.number_of_vertices):
            self._dfs(graph, vertex, 1)

    def _dfs(self, graph, vertex, depth):
        """
        Depth-first search to find Hamiltonian paths.
        
        Args:
            graph (Graph): The graph to perform DFS on.
            vertex (int): The current vertex being visited.
            depth (int): The current depth of the search.
        """
        self.marked[vertex] = True

        if depth == graph.number_of_vertices:
            self.count += 1

        for adjacent in graph.adjacency_lists[vertex]:
            if not self.marked[adjacent]:
                self._dfs(graph, adjacent, depth + 1)

        self.marked[vertex] = False


def main():
    """
    Main function to read a graph from a file and compute the number of Hamiltonian paths.
    """

    FILE_PATH = "data/euler_cycle.txt"
    graph = Graph.from_file(FILE_PATH)
    hamilton = HamiltonPath(graph)
    print(f"Number of Hamiltonian paths: {hamilton.count}")


if __name__ == "__main__":
    main()