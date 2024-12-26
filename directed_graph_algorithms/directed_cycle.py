from collections import deque
from digraph import *

class DirectedCycle:
    """
    A class to detect cycles in a directed graph.
    """

    def __init__(self, graph):
        """
        Initializes the DirectedCycle object and performs DFS to detect cycles.
        
        Args:
            graph (Digraph): The directed graph to check for cycles.
        """

        self.marked = [False] * graph.number_of_vertices
        self.on_stack = [False] * graph.number_of_vertices
        self.edge_to = [None] * graph.number_of_vertices
        self.cycle = deque()

        vertex = 0
        while vertex < graph.number_of_vertices and not self.has_cycle:
            if not self.marked[vertex]:
                self._dfs(graph, vertex)
            vertex += 1

    @property
    def has_cycle(self):
        """
        Checks if the graph has a cycle.
        
        Returns:
            bool: True if the graph has a cycle, False otherwise.
        """

        return bool(self.cycle)
    

    def _dfs(self, graph, vertex):
        """
        Recursively performs DFS to detect cycles in the graph.
        
        Args:
            graph (Digraph): The directed graph to check.
            vertex (int): The current vertex being visited.
        """

        self.marked[vertex] = True
        self.on_stack[vertex] = True
        for adjacent in graph.adjacency_lists[vertex]:
            if self.has_cycle:
                return

            if not self.marked[adjacent]:
                self.edge_to[adjacent] = vertex
                self._dfs(graph, adjacent)

            elif self.on_stack[adjacent]:
                self._get_cycle_path(vertex, adjacent)

        self.on_stack[vertex] = False

    def _get_cycle_path(self, vertex, adjacent):
        """
        Constructs the cycle path when a cycle is detected.
        
        Args:
            vertex (int): The current vertex where the cycle was detected.
            adjacent (int): The adjacent vertex that forms the cycle.
        """

        # Returns just one cycle path
        current = vertex
        while current is not None:
            self.cycle.appendleft(current)
            current = self.edge_to[current]
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
    Main function to read a directed graph from a file and check for cycles.
    """

    FILE_PATH = "data/digraph.txt"
    digraph = Digraph.from_file(FILE_PATH)
    dfs = DirectedCycle(digraph)
    print(f"Does the graph have cycles? {dfs.has_cycle}")
    print(f"Cycle detected: {dfs.get_cycle()}")


if __name__ == "__main__":
    main()