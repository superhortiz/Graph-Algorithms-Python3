from edge_weighted_graph import EdgeWeightedGraph
from utils.union_find import UnionFind
import heapq


class KruskalMST:
    """
    Implements Kruskal's algorithm to find the Minimum Spanning Tree (MST) of an edge-weighted graph.
    """

    def __init__(self, graph):
        """
        Initializes the KruskalMST object and computes the MST using Kruskal's algorithm.
        
        Args:
            graph (EdgeWeightedGraph): The edge-weighted graph to find the MST for.
        """
        self.mst = []
        priority_queue = []
        union_find = UnionFind(graph.number_of_vertices)

        for edge in graph.edges:
            heapq.heappush(priority_queue, edge)

        while priority_queue and len(self.mst) < graph.number_of_vertices - 1:
            edge = heapq.heappop(priority_queue)
            vertex_v = edge.either()
            vertex_w = edge.other(vertex_v)

            if not union_find.connected(vertex_v, vertex_w):
                union_find.union(vertex_v, vertex_w)
                self.mst.append(edge)

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
    using Kruskal's algorithm.
    """

    FILE_PATH = "data/ewg.txt"
    graph = EdgeWeightedGraph.from_file(FILE_PATH)
    mst = KruskalMST(graph)
    print(f"MST: {mst.edges()}")


if __name__ == "__main__":
    main()