Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 4.5
Date: 2021-10-28

---
# Implementing a stack in python
We can use python's `list` primitive data type and its methods to easily implement a stack.

```python

class Stack:

	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

```

This is how a [[What is a stack?|stack]] can be implemented manually. There is also a pip-installable package called `pythonds` which contains implementations of all standard data structures.

---
### See also:
- [[What is a stack?]]
- [[Stacks reverse the items they contain]]
- [[Operations of a stack]]