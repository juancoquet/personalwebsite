Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 4.22
Date: 2021-10-30

---
# Implementing an ordered list in python
We can implement an ordered list in a very similar way to how a [[Implementing a linked list in python|linked list]] is implemented. The only difference is that the `add` method must add the new item in the right place to maintain the order of the list, and the `insert` and `append` methods are no longer required. We can also optimise the `search` method if we choose, to take advantage of the fact that the list is ordered to minimise runtime.

```python
class Node:

def __init(self, data):
	self.data = data
	self.next = None
  

class OrderedList:
	def __init__(self):
		self.head = None

	def __iter__(self):
		current = self.head
		while current:
			yield current.data
			current = current.next

	def is_empty(self):
		return self.head == None

	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.next
		return count

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.data == item:
				found = True
			else:
				previous = current
				current = current.next
		if not previous:
			self.head = current.next
		else:
			previous.next = current.next
		return current.data
		
	def index(self, item):
		current = self.head
		idx = 0
		while current:
			if current.data == item:
			return idx
		else:
			current = current.next
			idx += 1

	def pop(self):
		current = self.head
		previous = None
		while current.next:
			previous = current
			current = current.next
		if previous:
			previous.next = None
		else:
			self.head = None
		return current.data

	def search(self, item):
		current = self.head
		found = False
		exceeded = False
		while current and not found and not exceeded:
			if current.data == item:
				found = True
			else:
				if current.data > item:
					stop = True
				else:
					current = current.next
		return found

	def add(self, item):
		current = self.head
		previous = None
		position_found = False
		while current and not position_found:
			if current.data > item:
				position_found = True
			else:
				previous = current
				current = current.next
		new_node = Node(item)
		if not previous:
			new_node.next = self.head
			self.head = new_node
		else:
			new_node.next = current
			previous.next = new_node

```

## `search(self, item)`
The modification made to search breaks the iteration loop if the value at the current node is greater than `item`. This is because, since the list is ordered, if `item` has not been found and the value of the current node is greater than `item`, all following nodes will also have values greater than `item` meaning that `item` does not exist in the list.

## `add(self, item)`
The `add` method needs to insert the new item in the right place in the list. To do this, it iterates through each node until either the value of the current node is greater than `item` or the current node becomes `None`, meaning that the end of the list has been reached. Once either of these conditions are met, the `previous` node is checked. If `previous` is `None`, that means that the new node must be inserted as the head of the list, and its `next` property assigned to the current head. If there is a previous node, the previous node must be set to point to the new node containing `item`.

---
### See also:
- [[What is an ordered list?]]
- [[Operations of an ordered list]]
- [[Implementing a linked list in python]]