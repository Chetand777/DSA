# Implementing a Priority Queue

"""
This is a collection of prioritized elements that allows arbitrary element insertion,
and allows the removal of the element that has first priority. When an element is
added to a priority queue, the user designates its priority by providing an associated
key. The element with the minimum key will be the next to be removed from the
queue

"""

class Empty(Exception): # Subclass Empty that inherits the properties from python's Exception class
  pass

class PriorityQueue():

  class item:

    def __init__(self, key, value):
      self.key = key
      self.value = value

    def __lt__(self, other):
      return self.key < other.key
    
  def is_empty(self):
    return len(self) == 0
  
# Implementing a Priority Queue with an Unsorted List

from positional_list.positional_list import PositionalList

class UnsortedPriorityQueue(PriorityQueue):

  def find_min(self):
    # Return Position of item with minimum key
    if self.is_empty():
      raise Empty('Priority queue is empty') 
    small = self.data.first()
    walk = self.data.after(small)
    while walk is not None:
      if walk.element < small.element:
        small = walk
        walk = self.data.after(walk)
    return small
  
  def __init__(self):
    self.data = PositionalList()

  def __len__(self):
    return len(self.data)

  def add(self, key, value):
    # Add a key-value pair
    self.data.add_last(self.item(key, value))

  def min(self):
    # Return key-value pair with minimum key
    p = self.find_min()
    items = p.element()
    return (items.key, items.value)
  
  def remove_min(self):
    # Remove and return key-value pair with minimum key
    p = self.find_min()
    items = self.data.delete(p)
    return (items.key, items.value)
  

# Implementation with a Sorted List

class SortedPriorityQueue(PriorityQueue):

  def __init__(self):
    self.data = PositionalList()

  def __len__(self):
    return len(self.data)
  
  def add(self, key, value):
    new = self.item(key, value)
    walk = self.data.last()
    while walk is not None and new < walk.element():
      walk = self.data.before(walk)
    if walk is None:
      self.data.add_first(new)
    else:
      self.data.add_after(walk, new)

  def min(self):
    if self.is_empty():
      raise Empty('Priority queue is empty')
    p = self.data.first()
    items = p.element()
    return (items.key, items.value)
  
  def remove_min(self):
    if self.is_empty():
      raise Empty('Priority queue is empty')
    p = self.data.first()
    items = self.data.delete(p)
    return (items.key, items.value)
  

# A min-oriented priority queue implemented with a binary heap

class HeapPriorityQueue(PriorityQueue):

  def parent(self, j):
    return (j - 1) // 2
  
  def left(self, j):
    return 2 * j + 1
  
  def right(self, j):
    return 2 * j + 2
  
  def has_left(self, j):
    return self.left(j) < len(self)
  
  def has_right(self, j):
    return self.right(j) < len(self)
  
  def swap(self, i, j):
    self._data[i], self._data[j] = self._data[j], self._data[i]

  def upheap(self, j):
    parent = self.parent(j)
    if j > 0 and self._data[j] < self._data[parent]:
      self.swap(j, parent)
      self.upheap(parent)

  def downheap(self, j):
    if self.has_left(j):
      left = self.left(j)
      smallest = left
      if self.has_right(j):
        right = self.right(j)
        if self.data[right] < self.data[left]:
          smallest = right
      if self.data[smallest] < self.data[j]:
        self.swap(j, smallest)
        self.downheap(smallest)

  def __init__(self):
    self.data = []

  def __len__(self):
    return len(self.data)
  
  def add(self, key, value):
    self.data.append(self.item(key, value))
    self.upheap(len(self.data) - 1)

  def min(self):
    item = self.data[0]
    return (item.key, item.value)
  
  def remove_min(self):
    if self.is_empty():
      raise Empty('Priority queue is empty')
    self.swap(0, len(self.data) - 1)
    item = self.data.pop()
    self.downheap(0)
    return (item.key, item.value)
