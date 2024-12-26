from digraph import *
from collections import deque


class SAP:
    """
    Implements the Shortest Ancestral Path (SAP) algorithm for finding the shortest common ancestor
    and the length of the shortest path in a directed graph.
    """

    def __init__(self, graph):
        """
        Initializes the SAP object with the given directed graph.
        
        Args:
            graph (Digraph): The directed graph to analyze.
        """

        self.graph = graph
        self._length = None
        self._sca = None

    @property
    def sca(self):
        """
        Returns the shortest common ancestor (SCA) of the last queried vertices.
        
        Returns:
            int: The vertex that is the SCA.
        """

        return self._sca

    @property
    def length(self):
        """
        Returns the length of the shortest path between the last queried vertices.
        
        Returns:
            int: The length of the shortest path.
        """

        return self._length

    def get_ancestor(self, vertex_v, vertex_w):
        """
        Finds the shortest common ancestor (SCA) of the given vertices and computes the length.
        
        Args:
            vertex_v (int or list): The first vertex or list of vertices.
            vertex_w (int or list): The second vertex or list of vertices.
        
        Returns:
            int: The vertex that is the SCA.
        """

        vertex_v, vertex_w = self._validate(vertex_v, vertex_w)
        self._sap(vertex_v, vertex_w)
        return self._sca

    def _validate(self, vertex_v, vertex_w):
        """
        Validates the input vertices to ensure they are within the graph's bounds.
        
        Args:
            vertex_v (int or list): The first vertex or list of vertices.
            vertex_w (int or list): The second vertex or list of vertices.
        
        Returns:
            tuple: A tuple of validated lists of vertices.
        
        Raises:
            ValueError: If any of the input vertices are invalid.
        """

        if isinstance(vertex_v, int):
            vertex_v = [vertex_v]

        if isinstance(vertex_w, int):
            vertex_w = [vertex_w]
        
        if not isinstance(vertex_v, list) or not vertex_v or not all(isinstance(vertex, int) \
                and 0 <= vertex < self.graph.number_of_vertices for vertex in vertex_v):
            raise ValueError("Invalid argument.")

        if not isinstance(vertex_w, list) or not vertex_w or not all(isinstance(vertex, int) \
                and 0 <= vertex < self.graph.number_of_vertices for vertex in vertex_w):
            raise ValueError("Invalid argument.")

        return vertex_v, vertex_w

    def _sap(self, vertex_v, vertex_w):
        """
        Computes the shortest ancestral path using bidirectional BFS.
        
        Args:
            vertex_v (list): The list of vertices from one side.
            vertex_w (list): The list of vertices from the other side.
        """

        self._sca = None
        self._length = float('inf')

        # Initialize data structures for bidirectional BFS
        queue_v, queue_w = deque(), deque()
        dist_to_v, dist_to_w = {}, {}
        visited_v, visited_w = set(), set()

        # To check if there are common elements in lists vertex_v and vertex_w
        set_check = set()

        for vertex in vertex_v:
            set_check.add(vertex)
            queue_v.append(vertex)
            dist_to_v[vertex] = 0
            visited_v.add(vertex)

        for vertex in vertex_w:
            # If there is a common element that element is the sca
            if vertex in set_check:
                self._sca = vertex_w
                self._length = 0
                return

            queue_w.append(vertex)
            dist_to_w[vertex] = 0
            visited_w.add(vertex)

            self._bidirectional_bfs(queue_v, queue_w, dist_to_v, dist_to_w, visited_v, visited_w)

            if self._sca is None:
                self._length = None

    def _bidirectional_bfs(self, queue_v, queue_w, dist_to_v, dist_to_w, visited_v, visited_w):
        """
        Performs bidirectional BFS from the source vertices.
        
        Args:
            queue_v (deque): The BFS queue for the first set of vertices.
            queue_w (deque): The BFS queue for the second set of vertices.
            dist_to_v (dict): The distances from the source vertices in vertex_v.
            dist_to_w (dict): The distances from the source vertices in vertex_w.
            visited_v (set): The set of visited vertices from vertex_v.
            visited_w (set): The set of visited vertices from vertex_w.
        """

        while queue_v or queue_w:
            if queue_v:
                self._bfs(queue_v, dist_to_v, dist_to_w, visited_v, visited_w)

            if queue_w:
                self._bfs(queue_w, dist_to_w, dist_to_v, visited_w, visited_v)

    def _bfs(self, queue, dist_to_current, dist_to_other, visited_current, visited_other):
        """
        Performs a single BFS step.
        
        Args:
            queue (deque): The BFS queue for the current set of vertices.
            dist_to_current (dict): The distances from the source vertices in the current set.
            dist_to_other (dict): The distances from the source vertices in the other set.
            visited_current (set): The set of visited vertices from the current set.
            visited_other (set): The set of visited vertices from the other set.
        """

        vertex = queue.popleft()

        for neighbor in self.graph.adjacents(vertex):
            if not neighbor in visited_current:
                queue.append(neighbor)
                visited_current.add(neighbor)
                dist_to_current[neighbor] = dist_to_current[vertex] + 1

                if neighbor in visited_other:
                    total_dist = dist_to_current[neighbor] + dist_to_other[neighbor]

                    if total_dist < self._length:
                        self._length = total_dist
                        self._sca = neighbor


def main():
    """
    Main function to read a directed graph from a file and find the shortest common ancestor.
    """

    FILE_PATH = "data/digraph25.txt"
    digraph = Digraph.from_file(FILE_PATH)
    sap = SAP(digraph)
    vertex_v = [13, 23, 24]
    vertex_w = [6, 16, 17]
    ancestor = sap.get_ancestor(vertex_v, vertex_w)
    print(f"Shortest common ancestor of subgroups of vertices {vertex_v} and {vertex_w} = {sap.sca}")
    print(f"Length = {sap.length}")


if __name__ == "__main__":
    main()