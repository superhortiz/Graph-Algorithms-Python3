from digraph import *
from collections import deque


class DirectedBFS:
    """
    Implements Breadth-First Search (BFS) for a directed graph.
    """

    def __init__(self, graph, source):
        """
        Initializes the DirectedBFS object and performs BFS from the source vertex.
        
        Args:
            graph (Digraph): The directed graph to perform BFS on.
            source (int): The source vertex from which to start the BFS.
        """

        self.marked = [False] * graph.number_of_vertices
        self.edge_to = [None] * graph.number_of_vertices
        self.dist_to = [0] * graph.number_of_vertices
        queue = deque()

        # Start
        queue.append(source)
        self.marked[source] = True
        
        while queue:
            vertex = queue.popleft()
            for adjacent in graph.adjacency_lists[vertex]:
                if not self.marked[adjacent]:
                    queue.append(adjacent)
                    self.marked[adjacent] = True
                    self.edge_to[adjacent] = vertex
                    self.dist_to[adjacent] = self.dist_to[vertex] + 1

    def has_path_to(self, vertex):
        """
        Checks if there is a path from the source vertex to the given vertex.
        
        Args:
            vertex (int): The target vertex.
        
        Returns:
            bool: True if there is a path, False otherwise.
        """

        return self.marked[vertex]

    def path_to(self, vertex):
        """
        Returns the path from the source vertex to the given vertex, if it exists.
        
        Args:
            vertex (int): The target vertex.
        
        Returns:
            str: A string representation of the path from the source to the target.
            None: If no path exists.
        """

        if not self.has_path_to(vertex):
            return None

        path = []
        current_vertex = vertex

        while current_vertex is not None:
            path.append(current_vertex)
            current_vertex = self.edge_to[current_vertex]
        return ' -> '.join(str(vertex) for vertex in reversed(path))


def main():
    """
    Main function to read a directed graph from a file, perform BFS, and print the path information.
    """

    FILE_PATH = "data/digraph.txt"
    digraph = Digraph.from_file(FILE_PATH)
    source = 7
    vertex = 1
    bfs = DirectedBFS(digraph, source)
    print(f"Is there a path from {source} to {vertex}? {bfs.has_path_to(vertex)}")
    print(f"Shortest path from {source} to {vertex}: {bfs.path_to(vertex)}")


if __name__ == "__main__":
    main()