# *********************************************************
# CLASS ELEMENT

# COLIN KELLEHER 117303363
# ASSIGNMENT 2 - CS2516
# *********************************************************


class Element:

# *********************************************************
# __init__
# Creating an element of a key, value and index
# *********************************************************
    def __init__(self, k, v, i):
        self._key = k  # initialising key
        self._value = v  # initialising value
        self._index = i  # initialising index

# *********************************************************
# __lt__
# Equality operation - less than
# *********************************************************
    def __lt__(self, other):
        return self._key < other._key

# *********************************************************
# __str__
# Return a string representation of the index
# *********************************************************
    def __str__(self):
        return "Value %i,Index %i,Key %i" % (self._value, self._index, self._key)

# *********************************************************
# GETTERS & SETTERS FOR KEY, VALUE & INDEX
# *********************************************************
    # GETTER & SETTER FOR KEY
    def getKey(self):
        return self._key

    def setKey(self, newkey):
        self._key = newkey

    # GETTER & SETTER FOR VALUE
    def getValue(self):
        return self._value

    def setValue(self, newvalue):
        self._value = newvalue

    # GETTER & SETTER FOR INDEX
    def getIndex(self):
        return self._index

    def setIndex(self, newindex):
        self._index = newindex

# *********************************************************
# _WIPE
# Reset the key, value, and index
# *********************************************************
    def _wipe(self):
        self._key = None
        self._value = None
        self._index = None
