# A Tree Abstract Base Class in Python
"""
Tree class being abstract, there is no reason to create a
direct instance of it, nor would such an instance be useful. The class exists to serve
as a base for inheritance, and users will create instances of concrete subclasses.

"""

"""
The operations that we can perform on Tree:
1) root()
2) parent(p)
3) num_children(p)
4) children(p)
5) is_empty()
6) len
7) iter
8) is_root(e)
9) is_leaf(e)
10) positions()

"""

class Tree:

  class Position:

    def element(self):
      # Return the element stored at this position
      return NotImplementedError('must be implemented by subclass')

    def __equal__(self, other):
      # Return true if other position represents the same location
      return NotImplementedError('must be implemented by subclass')
    
    def __noteqaul__(self, other):
      # Return true if other position does not represent the same location
      return not (self == other)
    
# ---------- abstract methods that concrete subclass must support ----------

  def root(self):
    # Return the root position of the tree (or None if tree is empty)
    return NotImplementedError('must be implemented by subclass')
  
  def parent(self, p):
    # Return the position of the parent of p, or None if p is root
    return NotImplementedError('must be implemented by subclass')
  
  def num_children(self, p):
    # Return the number of children of p
    return NotImplementedError('must be implemented by subclass')
  
  def children(self, p):
    # Return an iterable of positions representing the children of p
    return NotImplementedError('must be implemented by subclass')
  
  def __len__(self):
    # Return the total number of positions in the tree
    return NotImplementedError('must be implemented by subclass')
  
# ---------- concrete methods implimented ----------

  def is_root(self, p):
    # Return true if p is the root position
    return self.root() == p
  
  def is_leaf(self, p):
    # Return true if p is a leaf position
    return self.num_children(p) == 0
  
  def is_empty(self):
    # Return true if the tree is empty
    return len(self) == 0
  

# The BinaryTree Abstract Base Class in Python

class BinaryTree(Tree):

# ---------- abstract methods  ----------

  def left(self):
    # Return the position of the left child of the current position
    return NotImplementedError('must be implemented by subclass')
  
  def right(self):
    # Return the position of the right child of the current position
    return NotImplementedError('must be implemented by subclass')
  
# ---------- concrete methods ----------

  def sibling(self, p):
    # Return the position of the sibling of p, or None if p is the root or has no sibling
    parent = self.parent(p)
    if parent is None:
      return None
    else:
      if p == self.left(parent):
        return self.right(parent)
      else:
        return self.left(parent)
      
  def children(self, p):
    # Generate an iteration of Positions representing p s children.
    if self.left(p) is not None:
      yield self.left(p)
    if self.right(p) is not None:
      yield self.right(p)
    

# Linked Binary Tree imPlimentation

class LinkedBinaryTree(BinaryTree):

  class Node:
    def __init__(self, element, parent=None, left=None, right=None):
      self.element = element
      self.parent = parent
      self.left = left
      self.right = right

  class Position(BinaryTree.Position):
    def __init__(self, container, node):
      self.container = container
      self.node = node

    def element(self):
      # Return the element stored at this position
      return self.node.element

    def __equal__(self, other):
      # Return true if other position represents the same location
      return type(other) is type(self) and other.node is self.node
    
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
    return self.Position(self, node) if node is not None else None
  
# ------------ Binary Tree Constructor --------------

  def __init__(self):
    self.root = None
    self.size = 0

  def __len__(self):
    return self.size

  def root(self):
    return self.make_position(self.root)
  
  def parent(self, p):
    node = self.validate(p)
    return self.make_position(node)
  
  def left(self, p):
    node = self.validate(p)
    return self.make_position(node.left)
  
  def right(self, p):
    node = self.validate(p)
    return self.make_position(node.right)
  
  def num_children(self, p):
    node = self.validate(p)
    count = 0
    if node.left is not None:
      count += 1
    if node.right is not None:
      count += 1
    return count
  
  def add_root(self, e):
    # Create root for empty tree storing e as element and return the position of that root
    if self.root is not None:
      raise ValueError('root is present')
    self.size = 1
    self.root = self.Node(e)
    return self.make_position(self.root)
  
  def add_left(self, p, e):
    # Create a new left child for Position p, storing element e. Return the Position of new node.
    node = self.validate(p)
    if node.left is not None:
      raise ValueError('left child already exists')
    self.size += 1
    node.left = self.Node(e, node)
    return self.make_position(node.left)
  
  def add_right(self, p, e):
    # Create a new right child for Position p, storing element e. Return the Position of new node.
    node = self.validate(p)
    if node.right is not None:
      raise ValueError('right child already exists')
    self.size += 1
    node.right = self.Node(e, node)
    return self.make_position(node.right)
  
  def replace(self, p, e):
    # Replace the element at Position p with e and return the old element.
    node = self.validate(p)
    old = node.element
    node.element = e
    return old
  
  def delete(self, p):
    # Delete the node at Position p, and replace it with its child, if any. Return the element that had been stored at Position p. Raise ValueError if Position p is invalid or p has two children.
    node = self.validate(p)
    if self.num_children(p) == 2:
      raise ValueError('p has two children')
    child = node.left if node.left else node.right
    if child is not None:
      child.parent = node.parent
    if node is self.root:
      self.root = child
    else:
      parent = node.parent
      if node is parent.left:
        parent.left = child
      else:
        parent.right = child
    self.size -= 1
    node.parent = node
    return node.element
  
  def attach(self, p, t1, t2):
    # Attach trees t1 and t2 as left and right subtrees of external p
    node = self.validate(p)
    if not self.is_leaf(p):
      raise ValueError('p must be an external position')
    if not type(self) is type(t1) is type(t2):
      raise TypeError('Trees must be of the same type')
    self.size += len(t1) + len(t2)
    if not t1.is_empty():
      t1.root.parent = node
      node.left = t1.root
      t1.root = None
      t1.size = 0
    if not t2.is_empty():
      t2.root.parent = node
      node.right = t2.root
      t2.root = None
      t2.size = 0


