from digraph import Digraph
from topological_order import TopologicalOrder


class StrongComponents:
    """
    Implements the Kosaraju-Sharir algorithm to find strongly connected components
    in a directed graph.
    """

    def __init__(self, graph):
        """
        Initializes the StrongComponents object and performs the Kosaraju-Sharir algorithm.
        
        Args:
            graph (Digraph): The directed graph to analyze for strongly connected components.
        """

        self.marked = [False] * graph.number_of_vertices
        self.id = [None] * graph.number_of_vertices
        self._component = 0

        reversed_graph = Digraph.reverse_graph(graph)
        topological_sort = TopologicalOrder(reversed_graph)

        for vertex in reversed(topological_sort.reverse_postorder):
            if not self.marked[vertex]:
                self._dfs(graph, vertex, self._component)
                self._component += 1

    def _dfs(self, graph, vertex, component):
        """
        Recursively performs DFS to identify all vertices in the same component.
        
        Args:
            graph (Digraph): The graph to analyze.
            vertex (int): The current vertex being visited.
            component (int): The component identifier.
        """

        self.marked[vertex] = True
        self.id[vertex] = component
        for adjacent in graph.adjacency_lists[vertex]:
            if not self.marked[adjacent]:
                self._dfs(graph, adjacent, component)

    def connected(self, vertex_v, vertex_w):
        """
        Checks if two vertices are in the same strongly connected component.
        
        Args:
            vertex_v (int): The first vertex.
            vertex_w (int): The second vertex.
        
        Returns:
            bool: True if the vertices are in the same component, False otherwise.
        """

        return self.id[vertex_v] == self.id[vertex_w]

    def count(self):
        """
        Returns the number of strongly connected components in the graph.
        
        Returns:
            int: The number of strongly connected components.
        """

        return self._component

    def id_vertex(self, vertex):
        """
        Returns the component id of the given vertex.
        
        Args:
            vertex (int): The vertex to query.
        
        Returns:
            int: The component id of the vertex.
        """

        return self.id[vertex]
                

def main():
    """
    Main function to read a directed graph from a file and identify its strongly connected components.
    """

    FILE_PATH = "data/digraph.txt"
    graph = Digraph.from_file(FILE_PATH)
    dfs = StrongComponents(graph)
    print(f"Number of connected components: {dfs.count()}")
    vertex_v, vertex_w = 2, 10
    print(f"Vertex {vertex_v} connected to vertex {vertex_w}? {dfs.connected(vertex_v, vertex_w)}")
    print(f"Vertex {vertex_v} belongs to component: {dfs.id_vertex(vertex_v)}")
    print(f"Vertex {vertex_w} belongs to component: {dfs.id_vertex(vertex_w)}")


if __name__ == "__main__":
    main()