from edge_weighted_graph import EdgeWeightedGraph
from utils.index_min_pq import IndexMinPQ


class PrimMST:
    """
    Implements Prim's algorithm to find the Minimum Spanning Tree (MST) of an edge-weighted graph
    using an indexed minimum priority queue.
    """

    def __init__(self, graph):
        """
        Initializes the PrimMST object and computes the MST using Prim's algorithm.
        
        Args:
            graph (EdgeWeightedGraph): The edge-weighted graph to find the MST for.
        """
        self.marked = [False] * graph.number_of_vertices
        self.edge_to = [None] * graph.number_of_vertices
        self.dist_to = [float("inf")] * graph.number_of_vertices
        self.priority_queue = IndexMinPQ(graph.number_of_vertices)

        # Start with an arbitrary vertex
        source = 0
        self.dist_to[source] = 0.0
        self.priority_queue.insert(source, self.dist_to[source])

        while self.priority_queue:
            self._visit(graph, self.priority_queue.del_min())


    def _visit(self, graph, vertex_v):
        """
        Marks the vertex and updates the priority queue with the edges from this vertex.
        
        Args:
            graph (EdgeWeightedGraph): The graph to visit.
            vertex_v (int): The vertex to mark and visit its edges.
        """
        self.marked[vertex_v] = True

        for edge in graph.adjacents(vertex_v):
            vertex_w = edge.other(vertex_v)

            if self.marked[vertex_w]:
                continue

            if edge.weight < self.dist_to[vertex_w]:
                self.edge_to[vertex_w] = edge
                self.dist_to[vertex_w] = edge.weight

                if self.priority_queue.contains(vertex_w):
                    self.priority_queue.decrease_key(vertex_w, self.dist_to[vertex_w])
                else:
                    self.priority_queue.insert(vertex_w, self.dist_to[vertex_w])

    def edges(self):
        """
        Returns the edges in the Minimum Spanning Tree (MST).
        
        Returns:
            list: A list of edges in the MST.
        """
        return [edge for edge in self.edge_to if edge]


def main():
    """
    Main function to read an edge-weighted graph from a file and compute its Minimum Spanning Tree (MST)
    using Prim's algorithm.
    """

    FILE_PATH = "data/ewg.txt"
    graph = EdgeWeightedGraph.from_file(FILE_PATH)
    mst = PrimMST(graph)
    print(f"MST: {mst.edges()}")


if __name__ == "__main__":
    main()