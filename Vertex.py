# *********************************************************
# CLASS VERTEX

# COLIN KELLEHER 117303363
# ASSIGNMENT 2 - CS2516
# *********************************************************


class Vertex:
# *********************************************************
# __init__
# create a vertex with element
# *********************************************************

    def __init__(self, element):
        self._element = element

# *********************************************************
# __str__
# return a string representation fo the vertex
# *********************************************************
    def __str__(self):
        return str(self._element)

    __repr__ = __str__

# *********************************************************
# __lt__
# return True if this element is less than v's element
# *********************************************************
    def __lt__(self, v):
        return self._element < v.element()

# *********************************************************
# ELEMENT
# return the data for each vertex
# *********************************************************
    def element(self):
        return self._element
