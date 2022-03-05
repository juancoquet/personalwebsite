Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 14.17
Date: 2021-10-29

---
# Implementing a deque in python
We can use python's built-in `list` type to easily implement a deque.

```python 

class Deque:

	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def add_front(self, item):
		self.items.append(item)

	def add_rear(self, item):
		self.items.insert(0, item)

	def remove_front(self):
		return self.items.pop()

	def remove_rear(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

```

---
### See also:
- [[What is a deque?]]
- [[Operations of a deque]]