class EulerianGraph:
    """
    A class to identify and generate Eulerian tours and paths in an undirected graph.
    """

    def __init__(self, vertices):
        """
        Initializes the EulerianGraph object.
        
        Args:
            vertices (int): The number of vertices in the graph.
        """

        self._graph = {i: [] for i in range(vertices)}
        self._tour = []

    @property
    def euler_tour(self):
        """
        Returns the Eulerian tour if it exists.
        
        Returns:
            str: A string representation of the Eulerian tour if it exists, None otherwise.
        """

        if not self._valid_eulerian():
            return None
        
        # If the Eulerian tour has not yet been calculated, initiate its computation
        if not self._tour:
            self._get_euler_tour()

        return ' -> '.join(str(vertex) for vertex in self._tour)

    def add_edge(self, vertex_v, vertex_w):
        """
        Adds an edge between the specified vertices.
        
        Args:
            vertex_v (int): The first vertex.
            vertex_w (int): The second vertex.
        """

        self._graph[vertex_v].append(vertex_w)
        self._graph[vertex_w].append(vertex_v)

    def remove_edge(self, vertex_v, vertex_w):
        """
        Removes the edge between the specified vertices.
        
        Args:
            vertex_v (int): The first vertex.
            vertex_w (int): The second vertex.
        """

        self._graph[vertex_v].remove(vertex_w)
        self._graph[vertex_w].remove(vertex_v)

    def _get_euler_tour(self):
        """
        Computes the Eulerian tour if it exists.
        """

        # Start from 0 for a Eulerian cycle
        if self._has_eulerian_cycle():
            source = 0

        # Look for an odd vertex for a Eulerian path
        else:
            for vertex in range(len(self._graph)):
                if len(self._graph[vertex]) % 2 != 0:
                    source = vertex
                    break

        self._tour.append(source)
        self._dfs_euler(source)

    def _dfs_euler(self, vertex):
        """
        Recursively performs DFS to generate the Eulerian tour.
        
        Args:
            vertex (int): The current vertex being visited.
        """

        for adjacent in self._graph[vertex]:
            if self._edge_is_not_bridge(vertex, adjacent):
                self._tour.append(adjacent)
                self.remove_edge(vertex, adjacent)
                self._dfs_euler(adjacent)

    def _edge_is_not_bridge(self, vertex, neighbor):
        """
        Checks if an edge is not a bridge, i.e., its removal does not increase the number of connected components.
        
        Args:
            vertex (int): The first vertex of the edge.
            neighbor (int): The second vertex of the edge.
        
        Returns:
            bool: True if the edge is not a bridge, False otherwise.
        """

        # If the vertex has only one adjacent vertex (degree of 1),
        # it must be chosen as there are no other options
        if len(self._graph[vertex]) == 1:
            return True

        # Count the number of reachable vertices from vertex
        marked = [False] * len(self._graph)
        count = self._dfs_count(vertex, marked)

        # Count the number of reachable vertices from vertex when
        # the edge vertex-neighbor is removed
        self.remove_edge(vertex, neighbor)
        marked = [False] * len(self._graph)
        count_without_edge = self._dfs_count(vertex, marked)

        # restore the connection
        self.add_edge(vertex, neighbor)

        # If the edge vertex-neighbor is not a bridge, count doesn't have to change
        return count == count_without_edge

    def _dfs_count(self, vertex, marked):
        """
        Counts the number of reachable vertices from vertex recursively.
        
        Args:
            vertex (int): The starting vertex.
            marked (list of bool): List to keep track of visited vertices.
        
        Returns:
            int: The count of reachable vertices.
        """

        count = 1
        marked[vertex] = True
        for adjacent in self._graph[vertex]:
            if not marked[adjacent]:
                count += self._dfs_count(adjacent, marked)
        return count

    def _all_connected(self):
        """
        Checks if all vertices in the graph are connected.
        
        Returns:
            bool: True if all vertices are connected, False otherwise.
        """

        vertex = 0
        marked = [False] * len(self._graph)
        count = self._dfs_count(vertex, marked)
        return count == len(self._graph)

    def _number_of_odd_vertices(self):
        """
        Returns the number of vertices with an odd degree.
        
        Returns:
            int: The number of vertices with an odd degree.
        """

        number_of_odd_vertices = sum([1 for vertex in self._graph if len(self._graph[vertex]) % 2 != 0])
        return number_of_odd_vertices

    def _has_eulerian_cycle(self):
        """
        Checks if the graph has an Eulerian cycle.
        
        Returns:
            bool: True if the graph has an Eulerian cycle, False otherwise.
        """
        
        # Check if all vertices have even degree
        return self._number_of_odd_vertices() == 0

    def _has_eulerian_path(self):
        """
        Checks if the graph has an Eulerian path.
        
        Returns:
            bool: True if the graph has an Eulerian path, False otherwise.
        """

        # Check if exactly two vertices have odd degree
        return self._number_of_odd_vertices() == 2

    def _valid_eulerian(self):
        """
        Validates if the graph is either Eulerian or semi-Eulerian.
        
        Returns:
            bool: True if the graph is Eulerian or semi-Eulerian, False otherwise.
        """

        return self._all_connected() and (self._has_eulerian_path() or self._has_eulerian_cycle())

    @classmethod
    def from_file(cls, file_path):
        """
        Creates an EulerianGraph instance from a file.
        
        Args:
            file_path (str): The path to the file containing the graph data.
        
        Returns:
            EulerianGraph: An instance of the EulerianGraph class.
        """

        with open(file_path, 'r') as file:
            # Read the first two lines
            number_of_vertices = int(file.readline().rstrip())

            # Print the first two lines
            graph = cls(number_of_vertices)

            # Iterate over the rest of the file
            for line in file:
                vertex_v, vertex_w = map(int, line.rstrip().split())
                graph.add_edge(vertex_v, vertex_w)

            return graph


def main():
    """
    Main function to read a graph from a file and identify Eulerian tours or paths.
    """

    FILE_PATH = "data/euler_cycle.txt"
    print("Eulerian cycle or path:")
    graph = EulerianGraph.from_file(FILE_PATH)
    print(graph.euler_tour)


if __name__ == "__main__":
    main()