# Array based python queue implimentation
class Empty(Exception):
  pass

"""
The operations that we perform on the queue:
1) len()
2) is_empty()
3) first()
4) dequeue()
5) enqueue()
6) resize()

"""

class ArrayQueue:
  
  DEFAULT_CAPACITY = 10

  def __init__(self):
    # Create an empty queue initialized with None value for capacity
    self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0

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
    return self._data[self._front]
  
  def dequeue(self):
    # Remove and return the element at the front of the queue
    if self.is_empty():
      raise Empty('Queue is empty')
    element = self._data[self._front] # Element to remove from queue 1st element
    self._data[self._front] = None # After removing element from queue place None in that location to maintain data integrity

    self._front = (self._front + 1) % len(self._data) # Move the front pointer to next element using cicular buffer

    self._size -= 1
    return element
  
  def enqueue(self, item):
    # Add an element to the end of the queue
    if self._size == len(self._data): # Check if space available in queue
      self.resize(2*self._size) # Resize the queue to double size
    avail = (self._front + self._size) % len(self._data) # Calculate the next available position
    self._data[avail] = item
    self._size += 1

  def resize(self, new_capacity):
    # Resize the queue to new capacity
    old_capacity = self._data
    self._data = [None]*new_capacity
    for k in range(self._size):
      self._data[k] = old_capacity[self._front] # Copying the elements from old capacity queue to new capacity queue at correct position

      self._front = (self._front + 1) % len(self._data) # Move to the next element in the old array using circular buffer

    self._front = 0


# Test the implementation of Queue class

def test_queue():
    queue = ArrayQueue()

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

    # Test dequeue all elements
    print(queue.dequeue())  # Expected output: 20
    print(queue.is_empty())  # Expected output: True

    # Test dequeue on empty queue (should raise Empty exception)
    try:
        queue.dequeue()
    except Empty as e:
        print(e)  # Expected output: "Queue is empty"


test_queue()



  

