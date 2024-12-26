from collections import deque
from edge_weighted_digraph import EdgeWeightedDigraph


class EdgeWeightedCycleFinder:
    """
    A class to detect cycles in an edge-weighted directed graph.
    """

    def __init__(self, graph):
        """
        Initializes the EdgeWeightedCycleFinder object and performs DFS to detect cycles.
        
        Args:
            graph (EdgeWeightedDigraph): The edge-weighted directed graph to check for cycles.
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

    def _dfs(self, graph, vertex_v):
        """
        Recursively performs DFS to detect cycles in the graph.
        
        Args:
            graph (EdgeWeightedDigraph): The directed graph to check.
            vertex_v (int): The current vertex being visited.
        """
        self.marked[vertex_v] = True
        self.on_stack[vertex_v] = True

        for edge in graph.adjacency_lists[vertex_v]:
            if self.has_cycle:
                return

            vertex_w = edge.to_edge()

            if not self.marked[vertex_w]:
                self.edge_to[vertex_w] = vertex_v
                self._dfs(graph, vertex_w)

            elif self.on_stack[vertex_w]:
                self._get_cycle_path(vertex_v, vertex_w)

        self.on_stack[vertex_v] = False

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
        Returns the detected cycle as a list of vertices.
        
        Returns:
            list: A list of vertices in the cycle, if a cycle exists.
            None: If no cycle exists.
        """
        if not self.cycle:
            return None
        return list(self.cycle)


def main():
    """
    Main function to read an edge-weighted directed graph from a file and check for cycles.
    """

    FILE_PATH = "data/negative_cycle.txt"
    digraph = EdgeWeightedDigraph.from_file(FILE_PATH)
    dfs = EdgeWeightedCycleFinder(digraph)
    print(f"Does the graph have cycles? {dfs.has_cycle}")
    print(f"Cycle detected: {dfs.get_cycle()}")


if __name__ == "__main__":
    main()