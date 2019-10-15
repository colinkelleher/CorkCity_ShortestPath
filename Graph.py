# *********************************************************
# CLASS GRAPH

# COLIN KELLEHER 117303363
# ASSIGNMENT 2 - CS2516
# *********************************************************

# *********************************************************
# Import APQ, Vertex & Edge
# *********************************************************
from APQ import *
from Vertex import *
from Edge import *

# *********************************************************
# CLASS GRAPH
# Represents a simple graph
# init creates an empty graph
# *********************************************************


class Graph:

    def __init__(self):
        self._structure = dict()

# *********************************************************
# _str__ method
# return a string representation of the graph
# *********************************************************
    def __str__(self):
        hstr = ('|V| = ' + str(self.num_vertices())
                + '; |E| = ' + str(self.num_edges()))
        vstr = '\nVertices: '
        for v in self._structure:
            vstr += str(v) + '-'
        edges = self.edges()
        estr = '\nEdges: '
        for e in edges:
            estr += str(e) + ' '
        return hstr + vstr + estr

    __repr__ = __str__

# *********************************************************
# num_vertices
# return the number of vertices in the graph
# *********************************************************

    def num_vertices(self):
        return len(self._structure)

# *********************************************************
# num_edges
# return the number of edges in the graph
# *********************************************************
    def num_edges(self):
        num = 0
        for v in self._structure:
            num += len(self._structure[v])  # the dict of edges for v
        return num // 2  # divide by 2, since each edge appears in the
        # vertex list for both of its vertices

# *********************************************************
# vertices
# return a list of all vertices in entire graph
# *********************************************************
    def vertices(self):
        return [key for key in self._structure]

# *********************************************************
# get_vertex_by_label
# return the first vertex that matches the element passed
# *********************************************************
    def get_vertex_by_label(self, element):
        for v in self._structure:
            if v.element() == element:
                return v
        return None

# *********************************************************
# edges
# return a list of all edges in the entire graph
# *********************************************************
    def edges(self):
        edgelist = []
        for v in self._structure:
            for w in self._structure[v]:
                if self._structure[v][w].start() == v:
                    edgelist.append(self._structure[v][w])
        return edgelist

# *********************************************************
# get edges
# return a list of all edges incident on v
# *********************************************************
    def get_edges(self, v):
        if v in self._structure:
            edgelist = []
            for w in self._structure[v]:
                edgelist.append(self._structure[v][w])
            return edgelist
        return None

# *********************************************************
# get edge
# return the edge between v and w
# return None if no edge exists
# *********************************************************
    def get_edge(self, v, w):
        if (self._structure is not None
                and v in self._structure
                and w in self._structure[v]):
            return self._structure[v][w]
        return None

# *********************************************************
# degree
# return the degree of vertex v
# *********************************************************
    def degree(self, v):
        return len(self._structure[v])

# *********************************************************
# add_vertex
# Add a new vertex with data
# if vertex already exists with same data
    # a new vertex instance will be created
# *********************************************************
    def add_vertex(self, element):
        v = Vertex(element)
        self._structure[v] = dict()
        return v

# *********************************************************
# add_vertex_if_new
# Add & return vertex with element if not in graph - checks
# for equality between them, if there is special meaning to parts of the element
# this method may create multiple vertices with same id if
# any other parts of element are different. To ensure vertices
# are unique for individual parts of element, separate method
# needed
# *********************************************************
    def add_vertex_if_new(self, element):
        for v in self._structure:
            if v.element() == element:
                return v
        return self.add_vertex(element)

# *********************************************************
# add_edge
# add & return the edge between 2 vertices v & w with element
# if v or w are not vertices in graph, doesn't add & returns None
# If an edge between v and w already exists - previous edge
    # will be replaced
# *********************************************************
    def add_edge(self, v, w, element):
        if not v in self._structure or not w in self._structure:
            return None
        e = Edge(v, w, element)
        self._structure[v][w] = e
        self._structure[w][v] = e
        return e

# *********************************************************
# add_edge_pairs
# add all vertex pairs in elist as edges with empty elements
# *********************************************************
    def add_edge_pairs(self, elist):
        for (v, w) in elist:
            self.add_edge(v, w, None)

# *********************************************************
# Dijkstra's Algorithm
# from pseudocode
    # find all the shortest paths from s
    # locs is an empty dictionary ( keys are vertices, values are location in open)
    # preds starts as a dictionary with value for s = None
    # add s with key 0 to open
    # add s: element to locs
    # while open is not empty
    # remove the min element from open
    # remove the entry for vertex from locs & preds
    # add an entry for v :(cost, predecessor) into closed
    # for each edge e from v
    # w is the opposite vertex to v in e
    # if w is not in closed
    # newcost is v's key plus e's cost
    # if w is not in locs
    # add w:v to preds,
    # add w:newcost to open
    # add w:(elt returned from open) to locs
    # else if newcost is better than w's oldcost
    # update w:v in preds
    #  update w's cost in open to newcost
    # return closed
# *********************************************************
    def dijkstra(self, s): # s is starting position to find all the shortests paths from
        open = APQ() # open stars as an empty APQ
        locs = {} # Empty dictionary - keys are vertices, values are location in open)
        closed = {} # closed starts as an empty dictionary
        preds = {s: None} # preds starts as a dictionary with value for s = None
        element = open.addToHeap(0, s) # add s with key 0 to open
        locs[s] = element # add s: element to locs
        while open.length() is not 0: # while open is not empty
            apq = open.removemin()   # remove the min element from open
            vertex = apq._value # get vertex value
            cost = apq._key # initiate cost
            locs.pop(vertex) # remove the entry for vertex from locs
            predecessor = preds.pop(vertex) # remove the entry for vertex from preds
            closed[vertex] = (cost, predecessor)  # add an entry for v :(cost, predecessor) into closed
            for edge in self.get_edges(vertex): # for each edge e from v
                w = edge.opposite(vertex) # w is the opposite vertex to v in e
                if w not in closed: # if w is not in closed
                    new_cost = cost + edge._element # newcost is v's key plus e's cost
                    if w not in locs: # if w is not in locs
                        preds[w] = vertex #add w:v to preds,
                        element = open.addToHeap(new_cost, w) # add w:newcost to open,
                        locs[w] = element # add w:(elt returned from open) to locs
                    elif new_cost < open.get_key(locs[w]): # else if newcost is better than w's oldcost
                        preds[w] = vertex # update w:v in preds
                        open.update_key(locs[w], new_cost) #  update w's cost in open to newcost
        return closed

# *********************************************************
# Graph reader as given in Assignment
# for reading and returning the graphs
# simplegraph1.txt and simplegraph2.txt in this case
# *********************************************************

def graphreader(filename):
    graph = Graph()
    file = open(filename, 'r')
    entry = file.readline()  # either 'Node' or 'Edge'
    num = 0
    while entry == 'Node\n':
        num += 1
        nodeid = int(file.readline().split()[1])
        vertex = graph.add_vertex(nodeid)
        entry = file.readline()  # either 'Node' or 'Edge'
    print('Read', num, 'vertices and added into the graph')
    num = 0
    while entry == 'Edge\n':
        num += 1
        source = int(file.readline().split()[1])
        sv = graph.get_vertex_by_label(source)
        target = int(file.readline().split()[1])
        tv = graph.get_vertex_by_label(target)
        length = float(file.readline().split()[1])
        edge = graph.add_edge(sv, tv, length)
        file.readline()  # read the one-way data
        entry = file.readline()  # either 'Node' or 'Edge'
    print('Read', num, 'edges and added into the graph')
    print(graph)
    return graph

# *********************************************************
# Test Methods - Tests both * simplegraph1.txt * and
# * simplegraph2.txt *
# *********************************************************


def test():
    filename = 'simplegraph2.txt' #change filename here
    vertexLabel = 14 #change vertex label here
    print("****************\n%s\n****************" % filename)
    graph = graphreader(filename)  # read in the graph from the text file
    vertex = graph.get_vertex_by_label(vertexLabel)  # starting vertex on path you want to read (v1 to v4) - 1 as in assignment
    print(graph.dijkstra(vertex))

if __name__ == "__main__":
    test()  # call the test program
