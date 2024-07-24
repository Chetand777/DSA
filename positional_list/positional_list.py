"""
Positional List provides a user a way to refer to elements anywhere in a sequence, and to
perform arbitrary insertions and deletions

"""
# Positional List implimentation using Doubly Linked List

from deque_using_doubly_linked_list.deque import DoublyLinkedList

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
  


