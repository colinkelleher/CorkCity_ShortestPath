# *********************************************************
# CLASS APQ

# COLIN KELLEHER 117303363
# ASSIGNMENT 2 - CS2516
# *********************************************************

# *********************************************************
# Import everything from the Element class
# *********************************************************
from Element import *

# *********************************************************
# CLASS APQ
# Adaptable Priority Queue using a Binary Heap
# *********************************************************


class APQ:
# *********************************************************
#  Initialise the binary heap
# *********************************************************
    def __init__(self):
        self._binaryheap = [] # Creating the binary heap

# *********************************************************
#  __str__
# Return a string representation of the Key, Value & Index
# *********************************************************
    def __str__(self):
        result = ""
        for item in self._binaryheap:
            result += ("Key: %i, Value: %s, Index: %i \t" % (item._key, item._value, item._index))
        return result

# *********************************************************
# length
# return the length of the binary heap
# *********************************************************
    def length(self):
        return len(self._binaryheap)

# *********************************************************
# addToHeap
# add Key & Item to binary heap

    # note to self
    # from CS2515 - bubble up when adding element to binary heap
    # pseudocode on lecture 17 - the heap
    # add item in last position
    # bubbleup heap
    # update last position
# *********************************************************
    def addToHeap(self, key, item):
        if APQ.length(self) == 0: # if the length of the heap is zero
            index = 0 # initialise i to be zero
        else: # otherwise if the length is greater than 0
            index = APQ.length(self) # i is initialised to length of heap
        element = Element(key, item, index) # create the element
        self._binaryheap.append(element) # add this to the binary heap - append as it is a list
        if APQ.length(self) > 1: # if the size of the binary heap is greater than 1, run the bubble up heap sort
            self.bubbleUpHeap(element)
        return element
# *********************************************************
# swap
# Swap elements within the heap - used within bubble up and bubble down
# used for swapping elements when bubbling up and down
# *********************************************************

    def swap(self, element, other):
        index = element._index # get the index of the element
        other_index = other._index # get the index of the other element
        self._binaryheap[index] = other # index is equal to other index
        self._binaryheap[other_index] = element # other index is equal to element
        element._index = other_index # element index is equal to other index
        other._index = index #other index is equal to index
    # performing overall swap of element to other place and
    # other place to element place

# *********************************************************
# bubbleUpHeap
# needed when adding a value to the heap to restore property
# *********************************************************
    def bubbleUpHeap(self, element):
        index = (element._index - 1) // 2 # get the index - index -1 divided by 2
        if index >= 0 and index < APQ.length(self) - 1:
            parent = self._binaryheap[index] # get the parent
            if element._key < parent._key: # if the key of the element is less than the key of the parent
                self.swap(element, parent) # swap the parent and the element
                self.bubbleUpHeap(element) # recursively call the method
        return self._binaryheap # return the restored binary heap
# *********************************************************
# bubbleDownHeap
# recursive
# Needed when removing an element from the heap
# *********************************************************
    def bubbleDownHeap(self, element):
        index = element._index # get the index
        left = 2 * index + 1 # get the left index
        right = 2 * index + 2 # get the rifht index
        if left < APQ.length(self) and right < APQ.length(self): # left and right less than length
            if self._binaryheap[left]._key < self._binaryheap[right]._key: # left key less than right key
                if element._key > self._binaryheap[left]._key: # element greater than left index key
                    self.swap(element, self._binaryheap[left]) # swap element and left
                    self.bubbleDownHeap(element) # bubble the element down the heap
            elif element._key > self._binaryheap[right]._key: # key greater than right key
                    self.swap(element, self._binaryheap[right]) # swap element and right
                    self.bubbleDownHeap(element) # bubble the element down the heap
        elif left < APQ.length(self): #if left index is less than heap length
            if element._key > self._binaryheap[left]._key: # element key greatet than lefy key
                self.swap(element, self._binaryheap[left]) # swap left and element
                self.bubbleDownHeap(element) #bubble the element down the heap
        elif right < APQ.length(self): # right less than the heap length
            if element._key > self._binaryheap[right]._key: # element key greater than right key
                self.swap(element, self._binaryheap[right]) # swap the element and right
                self.bubbleDownHeap(element) # bubble the element down the heap
        return self._binaryheap # return the final heap

# *********************************************************
# Remove
# Remove an element from the binary heap
# *********************************************************
    def remove(self, element):
        if element == self._binaryheap[0]: # if the element is as the top of the binary heap
            self.removemin() # call remove min
        elif element == self._binaryheap[-1]: # if the element is at index minus 1
            self._binaryheap.pop() # pop this element off the binary heap
        else:
            index = element._index # get index
            left = 2 * index + 1 #left index
            right = 2 * index + 2 # right index
            parent = (index - 1)//2 # parent index
            lastindex = APQ.length(self)-1 #last index in the heap
            self._binaryheap[index],self._binaryheap[lastindex] = self._binaryheap[lastindex], self._binaryheap[index]
            self._binaryheap[index]._index = index
            self._binaryheap.pop(lastindex) # pop the last element
            if self._binaryheap[index]._key < self._binaryheap[parent]._key:
                # if the index is less than the parent
                self.bubbleUpHeap(self._binaryheap[index]) # bubble up the heap passing index
            elif (left < APQ.length(self)) or (right < APQ.length(self)):
                # if the  left index is less than length of heap  right index is less than length
                self.bubbleDownHeap(self._binaryheap[index])
            # bubble down the heap passing tbe index
# *********************************************************
# min
# Return the minimum value in the binary heap
# *********************************************************

    def min(self):
        return self._binaryheap[0]._value

# *********************************************************
# removemin
# Return the minimum value (top) in the binary heap

    # note to self
    # from CS2515 - bubble down element when removing from top
    # pseudocode on lecture 17 - the heap
    # root node is at index 0
    # last item is at index size-1
# *********************************************************
    def removemin(self):
        element = self._binaryheap[0] # get the minimum element
        if APQ.length(self) == 1: # if there is only one element in the binary heap
            self._binaryheap.pop(0)  # pop the minimum
        else:
            self._binaryheap[0] = self._binaryheap[-1] #update index zero
            self._binaryheap[0]._index = 0 # update the index of the minimum to be zero
            self._binaryheap.pop(-1) # pop it off the heap
            self.bubbleDownHeap(self._binaryheap[0]) # run bubble down on index zero of the binary heap
        return element # return

# *********************************************************
# balance
# ensure the heap is still a binary heap - and fix if not after performing specific operations
# *********************************************************
    def balance(self, element):
        index = element._index # get the index of the element
        parent = (-1)//2 # get the parent
        left = 2 * index + 1 # get the left of the index
        if index <= APQ.length(self)-1: # ift he length -1 is less than the index
            if parent >= 0: # check if the parent is less than or equal to zero
                if self._binaryheap[index]._key < self._binaryheap[parent]._key:
                    self.bubbleUpHeap(self._binaryheap[index])
            elif left < APQ.length(self): # if left index is less than
                self.bubbleDownHeap(self._binaryheap[index])
            return self._binaryheap # return the balanced binary heap
# *********************************************************
# is_empty
# Check to see if the binary heap is empty
# *********************************************************

    def is_empty(self):
        return self._binaryheap == []

# *********************************************************
# update_key
# Used within Dijkstra algorithm to update the key of an element
# *********************************************************
    def update_key(self, element, new_key):
        element._key = new_key
        self.balance(element)
# *********************************************************
# get_key
# Return the key of an element within the heap
# *********************************************************
    def get_key(self, element):
        return self._binaryheap[element._index]._key
