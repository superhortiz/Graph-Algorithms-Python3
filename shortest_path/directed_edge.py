class WeightedEdge:
    """
    Represents a weighted edge in a directed graph.
    """

    def __init__(self, vertex_v, vertex_w, weight):
        """
        Initializes a weighted edge with the specified vertices and weight.
        
        Args:
            vertex_v (int): One vertex of the edge.
            vertex_w (int): The other vertex of the edge.
            weight (float): The weight of the edge.
        """
        self._vertex_v = vertex_v
        self._vertex_w = vertex_w
        self._weight = weight

    @property
    def vertex_v(self):
        """
        Returns the source vertex of the edge.
        
        Returns:
            int: The source vertex.
        """
        return self._vertex_v

    @property
    def vertex_w(self):
        """
        Returns the destination vertex of the edge.
        
        Returns:
            int: The destination vertex.
        """
        return self._vertex_w

    @property
    def weight(self):
        """
        Returns the weight of the edge.
        
        Returns:
            float: The weight of the edge.
        """
        return self._weight

    def from_edge(self):
        """
        Returns the source vertex of the edge.
        
        Returns:
            int: The source vertex.
        """
        return self._vertex_v

    def to_edge(self):
        """
        Returns the destination vertex of the edge.
        
        Returns:
            int: The destination vertex.
        """
        return self._vertex_w

    def __lt__(self, other):
        """
        Compares this edge with another edge based on weight.
        
        Args:
            other (WeightedEdge): The other edge to compare with.
        
        Returns:
            bool: True if this edge's weight is less than the other edge's weight, False otherwise.
        """
        return self.weight < other.weight

    def __eq__(self, other):
        """
        Checks if this edge is equal to another edge based on weight.
        
        Args:
            other (WeightedEdge): The other edge to compare with.
        
        Returns:
            bool: True if the edges have the same weight, False otherwise.
        """
        return self.weight == other.weight

    def __repr__(self):
        """
        Returns a string representation of the edge.
        
        Returns:
            str: A string representation of the edge in the format "(vertex_v -> vertex_w, w = weight)".
        """
        return f"({self._vertex_v} -> {self._vertex_w}, w = {self.weight})"