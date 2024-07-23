# Implimenting queue with singly linked lists

class Empty(Exception):
  pass

class LinkedQueue:
  
  class Node: 
    def __init__(self, element, next):
      self.element = element
      self.next = next

  def __init__(self):
    # Create an empty queue 
    self._head = None
    self._tail = None
    self._size = 0

  def __len__(self):
    # Return the number of elements in the queue
    return self._size
  
  def is_empty(self):
    # Return True if the queue is empty, False otherwise
    return self._size == 0
  
  def first(self):
    # Return the element at the front of the queue without removing it
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._head.element
  
  def dequeue(self):
    # Remove and return the element at the front of the queue
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._head.element # Element to remove from queue 1st element
    self._head = self._head.next # After removing element from queue place next in that location to maintain data integrity

    self._size -= 1
    if self.is_empty():
      self._tail = None
    return answer
  
  def enqueue(self, item):
    # Add an element to the end of the queue
    newest_ele = self.Node(item, None)
    if self.is_empty():
      self._head = newest_ele
    else:
      self._tail.next = newest_ele

    self._tail = newest_ele
    self._size += 1


# Test the implementation of LinkedQueue class

def test_linked_queue():
    queue = LinkedQueue()

    # Test is_empty on an empty queue
    print(queue.is_empty())  # Expected output: True

    # Test enqueue and first
    queue.enqueue(10)
    print(queue.first())  # Expected output: 10
    print(queue.is_empty())  # Expected output: False

    # Test enqueue more elements
    queue.enqueue(20)
    print(queue.first())  # Expected output: 10

    # Test dequeue
    print(queue.dequeue())  # Expected output: 10
    print(queue.first())  # Expected output: 20
    print(queue.dequeue())  # Expected output: 20
    print(queue.is_empty())  # Expected output: True

    # Test dequeue on empty queue (should raise Empty exception)
    try:
        queue.dequeue()
    except Empty as e:
        print(e)  # Expected output: "Queue is empty"

test_linked_queue()