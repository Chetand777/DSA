# Implimenting Stack using python list
# Define a new exception class that is more appropriate to handle the errors

class Empty(Exception): # Subclass Empty that inherits the properties from python's Exception class
  pass

"""
The operations that we can perform on stacks:
1) len()
2) is_empty()
3) push()
4) top()
5) pop()

"""
class ArrayStack:
  def __init__(self):
    # Create empty stack
    self._data = []

  def __len__(self):
    # Return the number of elements in the stack
    return len(self._data)
  
  def is_empty(self):
    # Return True if the stack is empty, else False
    return len(self._data) == 0
  
  def push(self, value):
    # Add an element to the top of the stack
    self._data.append(value) # Add the element to the end of the list

  def top(self):
    # Return the top element of the stack without removing it
    if self.is_empty():
      raise Empty("Stack is empty")
    return self._data[-1] # Return the last element of the list
  
  def pop(self):
    # Remove and return the top element of the stack
    if self.is_empty():
      raise Empty("Stack is empty")
    return self._data.pop() # Remove and return the last element of the list
  