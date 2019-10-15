# *********************************************************
# CLASS EDGE
# Implemented with an order - can be used for directed or undirected graphs
# Job of graph class to handle them as directed or undirected

# COLIN KELLEHER 117303363
# ASSIGNMENT 2 - CS2516
# *********************************************************


class Edge:
# *********************************************************
# __init__
# create an edge between vertices v and w element
# *********************************************************

    def __init__(self, v, w, element):
        self._vertices = (v, w) # define / initiate the vertices
        self._element = element # define / initiate the element

# *********************************************************
# __str__
# return a string representation of the edge
# *********************************************************
    def __str__(self):
        return ('(' + str(self._vertices[0]) + '--'
                + str(self._vertices[1]) + ' : '
                + str(self._element) + ')')

    __repr__ = __str__
# *********************************************************
# vertices
# return n ordered paid of vertices for the edge
# *********************************************************

    def vertices(self):
        return self._vertices
# *********************************************************
# start
# return first vertex in ordered pair
# *********************************************************

    def start(self):
        return self._vertices[0]
# *********************************************************
# end
# return the second vertex in ordered pair
# *********************************************************

    def end(self):
        return self._vertices[1]
# *********************************************************
# opposite
# return the opposite vertex to v in the edge
# *********************************************************

    def opposite(self, v):
        if self._vertices[0] == v:
            return self._vertices[1]
        elif self._vertices[1] == v:
            return self._vertices[0]
        else:
            return None
# *********************************************************
# element
# return the element for the edge
# *********************************************************
    def element(self):
        return self._element