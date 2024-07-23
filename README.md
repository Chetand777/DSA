# Data Structures Implementation in Python

Welcome to my repository for fundamental data structures implemented from scratch in Python! This project includes implementations of various data structures, which are essential for efficient data handling and algorithmic processing.

## Overview

In this repository, you will find implementations of the following data structures:

- **Stack** 🏗️
- **LinkedStack** 🗂️
- **Queue** ⏳
- **LinkedQueue** 📥
- **CircularQueue** 🔄
- **LinkedDeque** 🔁

Each implementation is crafted from scratch to provide a deep understanding of how these data structures work and their applications.

## Data Structures

### 1. Stack 🏗️

**Definition:** A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. You add and remove elements from the top of the stack, similar to a stack of plates.

**Importance:** Stacks are crucial for algorithms like expression evaluation, function calls, undo mechanisms, and backtracking.

**File:** `stack.py`

### 2. LinkedStack 🗂️

**Definition:** A stack implemented using a singly linked list, where each node points to the next. This allows for dynamic memory allocation.

**Importance:** Offers efficient memory usage and operations compared to array-based stacks, especially for large datasets.

**File:** `linked_stack.py`

### 3. Queue ⏳

**Definition:** A queue is a linear data structure that follows the First In, First Out (FIFO) principle. Elements are added at the end and removed from the front, similar to a queue in a bank.

**Importance:** Essential for scenarios like scheduling, buffering, and breadth-first search algorithms.

**File:** `queue.py`

### 4. LinkedQueue 📥

**Definition:** A queue implemented using a singly linked list, where elements are added to the end and removed from the front.

**Importance:** Facilitates dynamic memory usage and efficient enqueue and dequeue operations.

**File:** `linked_queue.py`

### 5. CircularQueue 🔄

**Definition:** A circular queue is a queue where the end wraps around to the beginning, creating a circular structure.

**Importance:** Useful for scenarios with fixed-size buffers and round-robin scheduling, optimizing memory usage.

**File:** `circular_queue.py`

### 6. LinkedDeque 🔁

**Definition:** A deque (double-ended queue) implemented using a doubly linked list, allowing efficient insertion and deletion from both ends.

**Importance:** Versatile for applications needing quick access to both ends of a sequence, such as in scheduling and data manipulation.

**File:** `linked_deque.py`

