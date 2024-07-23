# Impliment stack with singly linked list

class Empty(Exception): 
  pass

class LinkedStack:
  class Node: # Single linked node to store the element
    def __init__(self, element, next):
      self.element = element
      self.next = next

  def __init__(self):
    # Create empty stack
    self._head = None
    self._size = 0

  def __len__(self):
    # Return the number of elements in the stack
    return self._size
  
  def is_empty(self):
    # Return True if the stack is empty, else False
    return self._size == 0
  
  def push(self, value):
    # Add an element to the top of the stack
    self._head = self.Node(value, self._head)
    self._size += 1

  def top(self):
    # Return the top element of the stack without removing it
    if self.is_empty():
      raise Empty("Stack is empty")
    return self._head.element
  
  def pop(self):
    # Remove and return the top element of the stack
    if self.is_empty():
      raise Empty("Stack is empty")
    answer = self._head.element
    self._head = self._head.next
    self._size -= 1
    return answer
  

# Test the implementation of LinkedStack class

def test_linked_stack():
    stack = LinkedStack()

    # Test is_empty on an empty stack
    print(stack.is_empty())  # Expected output: True

    # Test push and top
    stack.push(10)
    print(stack.top())  # Expected output: 10
    print(stack.is_empty())  # Expected output: False

    # Test push more elements
    stack.push(20)
    print(stack.top())  # Expected output: 20

    # Test pop
    print(stack.pop())  # Expected output: 20
    print(stack.top())  # Expected output: 10
    print(stack.pop())  # Expected output: 10
    print(stack.is_empty())  # Expected output: True

    # Test pop on empty stack (should raise Empty exception)
    try:
        stack.pop()
    except Empty as e:
        print(e)  # Expected output: "Stack is empty"

test_linked_stack()
