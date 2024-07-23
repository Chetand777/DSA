# Implementing a Queue with a Circularly Linked List

class Empty(Exception):
  pass

class CircularQueue:
  
  class Node: 
    def __init__(self, element, next):
      self.element = element
      self.next = next

  def __init__(self):
    # Create an empty queue 
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
    head = self._tail.next
    return head.element
  
  def dequeue(self):
    # Remove and return the element at the front of the queue
    if self.is_empty():
      raise Empty('Queue is empty')
    oldhead = self._tail.next
    if self._size == 1:
      self._tail = None
    else:
      self._tail.next = oldhead.next
    self._size -= 1
    return oldhead.element
  
  def enqueue(self, item):
    # Add an element to the end of the queue
    newest_ele = self.Node(item, None)
    if self.is_empty():
      newest_ele.next = newest_ele
    else:
      newest_ele.next = self._tail.next # new node points to head
      self._tail.next = newest_ele # old tail points to new node
    self._tail = newest_ele # update tail to new node
    self._size += 1
    
  def rotate(self):
    if self._size > 0:
      self._tail = self._tail.next # rotate the tail to the next node



# Test the implementation of CircularQueue class

def test_circular_queue():
    queue = CircularQueue()

    # Test is_empty on an empty queue
    print(queue.is_empty())  # Expected output: True

    # Test enqueue and first
    queue.enqueue(10)
    print(queue.first())  # Expected output: 10
    print(len(queue))  # Expected output: 1
    print(queue.is_empty())  # Expected output: False

    # Test enqueue more elements
    queue.enqueue(20)
    print(queue.first())  # Expected output: 10
    print(len(queue))  # Expected output: 2

    # Test dequeue
    print(queue.dequeue())  # Expected output: 10
    print(queue.first())  # Expected output: 20
    print(len(queue))  # Expected output: 1
    print(queue.dequeue())  # Expected output: 20
    print(queue.is_empty())  # Expected output: True

    # Test dequeue on empty queue (should raise Empty exception)
    try:
        queue.dequeue()
    except Empty as e:
        print(e)  # Expected output: "Queue is empty"

    # Test rotate
    queue.enqueue(30)
    queue.enqueue(40)
    print(queue.first())  # Expected output: 30
    queue.rotate()
    print(queue.first())  # Expected output: 40
    queue.rotate()
    print(queue.first())  # Expected output: 30

test_circular_queue()