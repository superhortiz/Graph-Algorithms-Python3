class FlowEdge:
    """
    Represents a flow edge in a flow network.
    """

    def __init__(self, vertex_v, vertex_w, capacity):
        """
        Initializes a flow edge with the specified vertices and capacity.
        
        Args:
            vertex_v (int): One vertex of the edge.
            vertex_w (int): The other vertex of the edge.
            capacity (float): The capacity of the edge.
        """
        self._vertex_v = vertex_v
        self._vertex_w = vertex_w
        self._capacity = capacity
        self._flow = 0.0

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
    def capacity(self):
        """
        Returns the capacity of the edge.
        
        Returns:
            float: The capacity of the edge.
        """
        return self._capacity

    @property
    def flow(self):
        """
        Returns the current flow through the edge.
        
        Returns:
            float: The current flow through the edge.
        """
        return self._flow

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
        if vertex == self.vertex_v:
            return self.vertex_w
        elif vertex == self.vertex_w:
            return self.vertex_v
        else:
            raise ValueError("Illegal endpoint")

    def residual_capacity_to(self, vertex):
        """
        Returns the residual capacity to the given vertex.
        
        Args:
            vertex (int): The target vertex.
        
        Returns:
            float: The residual capacity to the vertex.
        
        Raises:
            ValueError: If the given vertex is not one of the vertices of the edge.
        """
        if vertex == self.vertex_v:
            return self.flow
        elif vertex == self.vertex_w:
            return self.capacity - self.flow
        else:
            raise ValueError("Illegal endpoint")

    def add_residual_flow_to(self, vertex, delta):
        """
        Adds residual flow to the given vertex.
        
        Args:
            vertex (int): The target vertex.
            delta (float): The flow to be added.
        
        Raises:
            ValueError: If the given vertex is not one of the vertices of the edge.
        """
        if vertex == self.vertex_v:
            self._flow -= delta
        elif vertex == self.vertex_w:
            self._flow += delta
        else:
            raise ValueError("Illegal endpoint")

    def __repr__(self):
        """
        Returns a string representation of the flow edge.
        
        Returns:
            str: A string representation of the flow edge in the format "(vertex_v -(flow/capacity)-> vertex_w)".
        """
        return f"({self._vertex_v} -({self._flow}/{self._capacity})-> {self._vertex_w})"