Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 4.12
Date: 2021-10-29

---
# Implementing a queue in python
We can use python's primitive `list` type to easily implement a queue in python.

```python

class Queue:

	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		self.items.pop()

	def size(self):
		return len(self.items)

```

Notice that this implementation means that `enqueue` has a runtime function of **O(n)** since that is the runtime of the `list` type's `insert` method, while the `dequeue` runtime is **O(1)**.

---
### See also:
- [[What is a queue?]]
- [[Operations of a queue]]
- [[O(1) constant runtime function]]