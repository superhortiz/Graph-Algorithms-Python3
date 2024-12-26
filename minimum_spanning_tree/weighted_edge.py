class WeightedEdge:
    """
    Represents a weighted edge in an edge-weighted graph.
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
        Returns the first vertex of the edge.
        
        Returns:
            int: The first vertex.
        """
        return self._vertex_v

    @property
    def vertex_w(self):
        """
        Returns the second vertex of the edge.
        
        Returns:
            int: The second vertex.
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

    def either(self):
        """
        Returns one of the vertices of the edge.
        
        Returns:
            int: One of the vertices of the edge.
        """
        return self._vertex_v

    def other(self, vertex):
        """
        Returns the other vertex of the edge.
        
        Args:
            vertex (int): One vertex of the edge.
        
        Returns:
            int: The other vertex of the edge.
        
        Raises:
            ValueError: If the given vertex is not one of the vertices of the edge.
        """
        if vertex == self._vertex_v:
            return self._vertex_w
        return self._vertex_v

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
            str: A string representation of the edge in the format "(vertex_v - vertex_w, w = weight)".
        """
        return f"({self._vertex_v} - {self._vertex_w}, w = {self.weight})"