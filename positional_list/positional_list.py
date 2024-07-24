"""
Positional List provides a user a way to refer to elements anywhere in a sequence, and to
perform arbitrary insertions and deletions

"""
# Positional List implimentation using Doubly Linked List

class DoublyLinkedList:
  
  class Node: 
    def __init__(self, element, prev, next):
      self.element = element
      self.prev = prev
      self.next = next

  def __init__(self):
    # Create an empty queue 
    self.header = self.Node(None, None, None)
    self.trailer = self.Node(None, None, None)
    self.header.next = self.trailer
    self.trailer.prev = self.header
    self._size = 0

  def __len__(self):
    # Return the number of elements in the queue
    return self._size
  
  def is_empty(self):
    # Return True if the queue is empty, False otherwise
    return self._size == 0
  
  def insert_between(self, item, predecessor, successor): 
    # Add item between two existing nodes and return new node
    newest = self.Node(item, predecessor, successor)
    predecessor.next = newest
    successor.prev = newest
    self._size += 1
    return newest
  
  def delete_node(self, node):
    # Delete nonsentinel node from the list and return its element
    predecessor = node.prev
    successor = node.next
    predecessor.next = successor
    successor.prev = predecessor
    self._size -= 1
    element = node.element # record deleted element
    node.prev = node.next = node.element = None #  deprecate node
    return element 

# ---------------------------------------------------------------------------

class PositionalList(DoublyLinkedList):
  # Sequential container of elements allowing position access

  class Position:
    # Represent the location of single element

    def __init__(self, container, node):
      self.container = container
      self.node = node

    def element(self):
      # Return the element stored at this position
      return self.node.element

    def __equal__(self, other):
      # Return true if other position represents the same location
      return type(other) is type(self) and other.node is self.node
    
    def __noteqaul__(self, other):
      # Return true if other position does not represent the same location
      return not (self == other)
    
  def validate(self, p):
    # Return the position of the node
    if not isinstance(p, self.Position):
      raise TypeError('p must be a Position instance')
    if p.container is not self:
      raise ValueError('p does not belong to this container')
    if p.node.next is None:
      raise ValueError('p is no longer valid')
    return p.node
  
  def make_position(self, node):
    # Return a Position instance for a given node
    if node is self.header or node is self.trailer:
      return None
  
    return self.Position(self, node)
  
  def first(self):
    # Return the position of the first element in the list or None if list is empty
    return self.make_position(self.header.next)
  
  def last(self):
    # Return the position of the last element in the list or None if list is empty
    return self.make_position(self.trailer.prev)
  
  def before(self, p):
    # Return the position just before the given position or None if p is first position
    node = self.validate(p)
    return self.make_position(node.prev)
  
  def after(self, p):
    # Return the position just after the given position or None if p is last position
    node = self.validate(p)
    return self.make_position(node.next)
  
  def iter(self, p):
    # Generate an iterator for the elements in the list starting at position p
    cursor = self.first()
    while cursor is not None:
      yield cursor.element()
      cursor = self.after(cursor)

# ------------------- Overridden Methods ------------------------------------------
  
  def insert_between(self, e, predecessor, successor):
    # Insert element e between two existing positions
    node = super().insert_between(e, predecessor, successor)
    return self.make_position(node)
  
  def add_first(self, e):
    # Insert element e at the front of the list and return its position
    return self.insert_between(e, self.header, self.header.next)
  
  def add_last(self, e):
    # Insert element e at the end of the list and return its position
    return self.insert_between(e, self.trailer.prev, self.trailer)
  
  def add_before(self, p, e):
    # Insert element e before the given position and return its position
    node = self.validate(p)
    return self.insert_between(e, node.prev, node)
  
  def add_after(self, p, e):
    # Insert element e after the given position and return its position
    node = self.validate(p)
    return self.insert_between(e, node, node.next)
  
  def delete(self, p):
    # Delete the element at the given position and return it
    node = self.validate(p)
    return self.delete_node(node)
  
  def replace(self, p, e):
    # Replace the element at the given position with e and return the old element
    node = self.validate(p)
    old_element = node.element
    node.element = e
    return old_element
  
# ------------------------------------------------------------------------------------------------

# Test and Impliment PositionalList class

def test_positional_list():
    # Initialize the positional list
    pl = PositionalList()

    # Test add_first and first
    p1 = pl.add_first(10)
    assert p1.element() == 10
    assert pl.first().element() == 10

    # Test add_last and last
    p2 = pl.add_last(20)
    assert p2.element() == 20
    assert pl.last().element() == 20

    # Test add_before
    p3 = pl.add_before(p2, 15)
    assert p3.element() == 15
    assert pl.before(p2).element() == 15

    # Test add_after
    p4 = pl.add_after(p1, 12)
    assert p4.element() == 12
    assert pl.after(p1).element() == 12

    # Test iter
    elements = [element for element in pl.iter(pl.first())]
    assert elements == [10, 12, 15, 20]

    # Test replace
    old_value = pl.replace(p1, 5)
    assert old_value == 10
    assert p1.element() == 5
    assert pl.first().element() == 5

    # Test delete
    deleted_value = pl.delete(p1)
    assert deleted_value == 5
    assert pl.first().element() == 12

    # Validate list order after deletions
    elements = [element for element in pl.iter(pl.first())]
    assert elements == [12, 15, 20]

    print("All tests passed!")

# Run the test function
test_positional_list()

