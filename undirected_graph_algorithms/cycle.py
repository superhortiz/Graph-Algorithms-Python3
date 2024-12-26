from graph import *
from collections import deque


class Cycle:
    """
    A class to detect cycles in an undirected graph.
    
    Assumes no self-loops or parallel edges.
    """

    def __init__(self, graph):
        """
        Initializes the Cycle object and performs DFS to detect cycles.
        
        Args:
            graph (Graph): The graph to check for cycles.
        """

        self.marked = [False] * graph.number_of_vertices
        self.edge_to = [None] * graph.number_of_vertices
        self.cycle = deque()

        vertex = 0
        while vertex < graph.number_of_vertices and not self.has_cycle:
            if not self.marked[vertex]:
                self._dfs(graph, vertex, -1)
            vertex += 1

    @property
    def has_cycle(self):
        """
        Checks if the graph has a cycle.
        
        Returns:
            bool: True if the graph has a cycle, False otherwise.
        """

        return bool(self.cycle)

    def _dfs(self, graph, current_vertex, parent_vertex):
        """
        Recursively performs DFS to detect cycles in the graph.
        
        Args:
            graph (Graph): The graph to check.
            current_vertex (int): The current vertex being visited.
            parent_vertex (int): The parent vertex of the current vertex.
        """

        self.marked[current_vertex] = True
        for adjacent in graph.adjacency_lists[current_vertex]:
            if self.has_cycle:
                return

            if not self.marked[adjacent]:
                self.edge_to[adjacent] = current_vertex
                self._dfs(graph, adjacent, current_vertex)

            elif adjacent != parent_vertex:
                # Adjacent is marked and is not the parent vertex
                # Then a cycle has been found
                self._get_cycle_path(current_vertex, adjacent)

    def _get_cycle_path(self, current_vertex, adjacent):
        """
        Constructs the cycle path when a cycle is detected.
        
        Args:
            current_vertex (int): The current vertex where the cycle was detected.
            adjacent (int): The adjacent vertex that forms the cycle.
        """

        # Returns just one cycle path
        vertex = current_vertex
        while vertex is not None:
            self.cycle.appendleft(vertex)
            vertex = self.edge_to[vertex]
        self.cycle.append(adjacent)

    def get_cycle(self):
        """
        Returns the detected cycle as a string representation.
        
        Returns:
            str: A string representation of the cycle path, if a cycle exists.
            None: If no cycle exists.
        """

        if not self.cycle:
            return None
        return ' -> '.join(str(vertex) for vertex in self.cycle)


def main():
    """
    Main function to read a graph from a file and check for cycles.
    """

    FILE_PATH = "data/euler_cycle.txt"
    graph = Graph.from_file(FILE_PATH)
    dfs = Cycle(graph)
    print(f"Does the graph have cycles? {dfs.has_cycle}")
    print(f"Cycle detected: {dfs.get_cycle()}")


if __name__ == "__main__":
    main()