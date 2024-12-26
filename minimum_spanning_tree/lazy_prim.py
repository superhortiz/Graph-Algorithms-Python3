from edge_weighted_graph import EdgeWeightedGraph
import heapq


class LazyPrimMST:
    """
    Implements Lazy Prim's algorithm to find the Minimum Spanning Tree (MST) of an edge-weighted graph.
    """

    def __init__(self, graph):
        """
        Initializes the LazyPrimMST object and computes the MST using Lazy Prim's algorithm.
        
        Args:
            graph (EdgeWeightedGraph): The edge-weighted graph to find the MST for.
        """
        self.mst = []
        self.priority_queue = []
        self.marked = [False] * graph.number_of_vertices

        # Start with an arbitrary vertex
        source = 0
        self._visit(graph, source)

        # Process the priority queue until we have enough edges for the MST
        while self.priority_queue and len(self.mst) < graph.number_of_vertices - 1:
            edge = heapq.heappop(self.priority_queue)
            vertex_v = edge.either()
            vertex_w = edge.other(vertex_v)

            # Skip if both vertices are already marked
            if self.marked[vertex_v] and self.marked[vertex_w]:
                continue

            # Add the edge to the MST
            self.mst.append(edge)

            # Visit the vertices that are not yet marked
            if not self.marked[vertex_v]:
                self._visit(graph, vertex_v)

            if not self.marked[vertex_w]:
                self._visit(graph, vertex_w)


    def _visit(self, graph, vertex):
        """
        Marks the vertex and adds all edges from this vertex
        to the priority queue if the other endpoint is not marked.
        
        Args:
            graph (EdgeWeightedGraph): The graph to visit.
            vertex (int): The vertex to mark and visit its edges.
        """
        self.marked[vertex] = True
        for edge in graph.adjacents(vertex):
            if not self.marked[edge.other(vertex)]:
                heapq.heappush(self.priority_queue, edge)

    def edges(self):
        """
        Returns the edges in the Minimum Spanning Tree (MST).
        
        Returns:
            list: A list of edges in the MST.
        """
        return self.mst


def main():
    """
    Main function to read an edge-weighted graph from a file and compute its Minimum Spanning Tree (MST)
    using Lazy Prim's algorithm.
    """

    FILE_PATH = "data/ewg.txt"
    graph = EdgeWeightedGraph.from_file(FILE_PATH)
    mst = LazyPrimMST(graph)
    print(f"MST: {mst.edges()}")


if __name__ == "__main__":
    main()