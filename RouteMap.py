# *********************************************************
# COLIN KELLEHER
# *********************************************************
from APQ import *
from Vertex import *
from Edge import *
# *********************************************************
# Class RouteMap
# *********************************************************


class RouteMap:
    def __init__(self):
        # created three separate dictionaries for ease of access
        self._structure = dict()
        self._elements = dict()  # dictionary to hold elements
        # keys = vertices
        # values = vertices
        self._coordinates = dict() # create a dictionary to hold coordinates
        # keys = vertices
        # values = edges
        # used for easier access

# *********************************************************
# _str__ method
# return a string representation of the graph
# *********************************************************
    def __str__(self):
        if self.num_vertices() <= 100 and self.num_edges() <= 100:
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
        if self._elements[element]:
            return self._elements[element]
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
        if (None is not self._structure
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
    def add_vertex(self, element, coordinates):
        v = Vertex(element)
        self._structure[v] = dict()
        self._coordinates[v] = coordinates
        # add vertex v with associated coordinates to dict
        self._elements[element] = v
        # add vertex v to dict with element as key
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
# sp(self, v, w) - shortest path
# Method * sp(self, v, w) * which will call my implementation
# of Dikstra's from source v and receive the table in return
# Create a list of the vertices and their costs in the path from v to w
# List built traversing backwards from the entry for w until v is reached
# list is then reversed
# *********************************************************
    def sp(self, v, w):
        dijks = self.dijkstra(v)  # call implementation of Dijkstra's method from source v
        vertex = None # initiate the vertex to be none
        result = []  # create a list of the result
        value = dijks[w]  # value is value of w in what is returned to variable dijks
        cost = value[0]  # cost of path is the value at index 0 of value
        preceding = value[1]  # the preceding value, is the value at index 1 of value
        result += [(w, cost)]
        while vertex is not v:  # while the vertex is not equal to inputted value v
            vertex = preceding # vertex is now equal to the preceding value
            value = dijks[preceding] # value is value of preceding in what is returned by dijks
            cost = value[0] # cost of path is the value at index 0 of value
            preceding = value[1] # the preceding value, is the value at index 1 of value
            result += [(vertex, cost)] # add the vertex and the cost to the result list
        return result[::-1]  # reverse the list using list slicing
# *********************************************************
# METHOD TO PRINT OUT THE PATH, ONE VERTEX PER LINE
# printvlist - as in test routine
# *********************************************************
    def printvlist(self, path):
        print("type\tlatitude\tlongitude\telement\t\tcost")
        for value in path: # for each item in the path passed into method
            index = value[0] # get the index of the item, starting at the front and incrementing through with the loop
            print("W\t%f\t%f\t%i\t%f" % (self._coordinates[index][0], self._coordinates[index][1], index._element, value[1])) # print latitude, longitude, element, cost
# self._coordinates[index][0] = latitude
# self._coordinates[index][1] = longitude
# index._element = element
# value [1] = cost
# *********************************************************
# Graph reader
# for reading and returning the route map
# *********************************************************

def graphreader(filename):
    route = RouteMap()
    file = open(filename, 'r')
    entry = file.readline()  # either 'Node' or 'Edge'
    num = 0
    while entry == 'Node\n':
        num += 1
        nodeid = int(file.readline().split()[1])
        entry = file.readline().split()  # line with GPS details
        coords = (float(entry[1]), float(entry[2]))  # latitude, longitude
        vertex = route.add_vertex(nodeid, coords)
        entry = file.readline()  # either 'Node' or 'Edge'
    print('Read', num, 'vertices and added into the graph')
    num = 0
    while entry == 'Edge\n':
        num += 1
        source = int(file.readline().split()[1])
        sv = route.get_vertex_by_label(source)
        target = int(file.readline().split()[1])
        tv = route.get_vertex_by_label(target)
        length = float(file.readline().split()[1])
        edge = route.add_edge(sv, tv, length)
        time = float(file.readline().split()[1])
        file.readline()  # read the one-way data
        entry = file.readline()  # either 'Node' or 'Edge'
    print('Read', num, 'edges and added into the graph')

    return route


# *********************************************************
# TEST DATA 
# *********************************************************

def test():
    routemap = graphreader('corkCityData.txt')
    ids = {}
    ids['wgb'] = 1669466540
    ids['turnerscross'] = 348809726
    ids['neptune'] = 1147697924
    ids['cuh'] = 860206013
    ids['oldoak'] = 358357
    ids['gaol'] = 3777201945
    ids['mahonpoint'] = 330068634
    sourcestr = 'wgb'
    deststr = 'neptune'
    print("Route -> from: %s to: %s" % (sourcestr, deststr))
    source = routemap.get_vertex_by_label(ids[sourcestr])
    dest = routemap.get_vertex_by_label(ids[deststr])
    tree = routemap.sp(source, dest)
    routemap.printvlist(tree)

if __name__ == "__main__":
    test()
