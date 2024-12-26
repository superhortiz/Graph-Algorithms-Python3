from flow_network import FlowNetwork
from collections import deque


class FordFulkerson:
    """
    Implements the Ford-Fulkerson algorithm to compute the maximum flow in a flow network.
    """

    def __init__(self, digraph, source, target):
        """
        Initializes the FordFulkerson object and computes the maximum flow from the source to the target vertex.
        
        Args:
            digraph (FlowNetwork): The flow network.
            source (int): The source vertex.
            target (int): The target vertex.
        """
        self._edge_to = [None] * digraph.number_of_vertices
        self._marked = [False] * digraph.number_of_vertices
        self._value = 0.0

        while self._has_augmenting_path(digraph, source, target):
            bottle = float('inf')
            current = target

            while current != source:
                bottle = min(bottle, self._edge_to[current].residual_capacity_to(current))
                current = self._edge_to[current].other(current)

            current = target
            while current != source:
                self._edge_to[current].add_residual_flow_to(current, bottle)
                current = self._edge_to[current].other(current)

            self._value += bottle

    @property
    def value(self):
        """
        Returns the value of the maximum flow.
        
        Returns:
            float: The value of the maximum flow.
        """
        return self._value

    @property
    def in_cut(self):
        """
        Returns the vertices in the minimum cut.
        
        Returns:
            list: A list of vertices in the minimum cut.
        """
        return [vertex for vertex in range(len(self._marked)) if self._marked[vertex]]

    def _has_augmenting_path(self, digraph, source, target):
        """
        Checks if there is an augmenting path from source to target using BFS.
        
        Args:
            digraph (FlowNetwork): The flow network.
            source (int): The source vertex.
            target (int): The target vertex.
        
        Returns:
            bool: True if there is an augmenting path, False otherwise.
        """

        # Reset the lists
        self._edge_to[:] = [None] * len(self._edge_to)
        self._marked[:] = [False] * len(self._marked)

        # Implement the BFS to find an augmenting path
        queue = deque([source])
        self._marked[source] = True

        while queue:
            vertex_v = queue.popleft()
            for edge in digraph.adjacents(vertex_v):
                vertex_w = edge.other(vertex_v)
                if edge.residual_capacity_to(vertex_w) > 0 and not self._marked[vertex_w]:
                    self._edge_to[vertex_w] = edge
                    self._marked[vertex_w] = True
                    queue.append(vertex_w)

        return self._marked[target]


def main():
    """
    Main function to read a flow network from a file and compute the maximum flow using the Ford-Fulkerson algorithm.
    """

    FILE_PATH = "data/fn.txt"
    network = FlowNetwork.from_file(FILE_PATH)
    source = 0
    target = 7
    ford_fulkerson = FordFulkerson(network, source, target)
    print(f"Maximum flow of the network = {ford_fulkerson.value}")
    print(f"Vertices in minimum cut: {ford_fulkerson.in_cut}")


if __name__ == "__main__":
    main()