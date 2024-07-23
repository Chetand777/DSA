#  Basic Implementation of a Doubly Linked List

class Empty(Exception):
  pass

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
  
# Implementing a Deque with a Doubly Linked List

class LinkedDeque(DoublyLinkedList):

  def first(self):
    # Return the element at the front of the deque without removing it
    if self.is_empty():
      raise Empty('Deque is empty')
    return self.header.next.element
  
  def last(self):
    # Return the element at the end of the deque without removing it
    if self.is_empty():
      raise Empty('Deque is empty')
    return self.trailer.prev.element
  
  def add_first(self, item):
    # Add item to the front of the deque
    self.insert_between(item, self.header, self.header.next)

  def add_last(self, item):
    # Add item to the end of the deque
    self.insert_between(item, self.trailer.prev, self.trailer)

  def delete_first(self):
    # Remove and return the element at the front of the deque
    if self.is_empty():
      raise Empty('Deque is empty')
    return self.delete_node(self.header.next)
  
  def delete_last(self):
    # Remove and return the element at the end of the deque
    if self.is_empty():
      raise Empty('Deque is empty')
    return self.delete_node(self.trailer.prev)
  


# Create an instance of LinkedDeque
deque = LinkedDeque()

# Test adding elements to the deque
print("Adding elements to deque...")
deque.add_first(10)
deque.add_last(20)
deque.add_first(5)
deque.add_last(30)

# Print the first and last elements
print("First element:", deque.first())  # Should print 5
print("Last element:", deque.last())   # Should print 30

# Test removing elements from the deque
print("Removing elements from deque...")
print("Removed first element:", deque.delete_first())  # Should print 5
print("Removed last element:", deque.delete_last())    # Should print 30

# Print the current first and last elements
print("Current first element:", deque.first())  # Should print 10
print("Current last element:", deque.last())   # Should print 20

# Remove the remaining elements
print("Removing last elements...")
print("Removed first element:", deque.delete_first())  # Should print 10
print("Removed last element:", deque.delete_last())    # Should print 20

# Test if the deque is empty
print("Is deque empty?", deque.is_empty())  # Should print True
