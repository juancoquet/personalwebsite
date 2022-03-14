---
aliases: [linked list, linked lists]
Date: 2021-10-29
---
Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 14.21

---
# Implementing a linked list in python
A linked list is comprised of nodes, each of which holds information about its own data and a pointer to the next node in the chain. This means that as long as we know where to find the first node, we will have all the information required to reach the last node in the linked list. The last node in the chain also needs to be aware that there is no next node.

```python

class Node:
	
	def __init__(self, data):
		self.data = data
		self.next = None
		
```

In python we can get and set attribute values by accessing the attribute with dot-notation directly, but there are certain use cases where getter and setter functions may be required.

Now that the `Node` class is in place, we can create a `LinkedList` class to string multiple nodes together. Here is how it looks:

```python
class LinkedList:

	def __init__(self):
		self.head = None

	def __iter__(self):
		current = self.head
		while current:
			yield current.data
			current = current.next

	def is_empty(self):
		return self.head == None

	def add(self, item):
		new_node = Node(item)
		new_node.next = self.head
		self.head = new_node

	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.next
		return count

	def search(self, item):
		current = self.head
		found = False
		while current and not found:
			if current.data == item:
				found = True
			else:
			current = current.next
		return found

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

	def append(self, item):
		current = self.head
		while current.next:
			current = current.nex
		current.next = Node(item)

	def insert(self, index, item):
		current = self.head
		previous = None
		idx = 0
		while idx != index:
			previous = current
			current = current.next
			idx += 1
		new_node = Node(item)
		new_node.next = current
		if previous:
			previous.next = new_node
		else:
			self.head = new_node

	def index(self, item):
		current = self.head
		idx = 0
		found = False
		while not found:
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

```

## `__init__(self)`
The `__init__` method sets the head of the linked list to `None` by default. This value will change when we add nodes using the `add` method later.

## `__iter__(self)`
The `__iter__` method makes our linked list iterable, meaning that we can use it with `for` loops. We have a `current` value, which is first set to the head node, the first node in the list (if any). Next, we use a `while` loop to `yield` the data of the current node before changing `current` to the next node in the list. The `while` loop will break when the last node in the list changes the value of current to its `.next` attribute, which is set to `None`.

## `is_empty(self)`
Checks if a head node is present. If there is no head node, it means that the list is empty. Returns a boolean.

## `add(self, item)`
Creates a new node containing the data provided in `item` and adds it to the beginning of the linked list. It sets the `next` attribute of the new node containing `item` to point to the current head of the list, then makes the new node the head of the list.

## `size(self)`
Starting at the head of the list, the `size` method uses a `while` loop to traverse through each node in the list and increments a `count` variable with each node visited. The loop breaks when `current` is set to `None`, meaning that the last node has been visited.

## `search(self, item)`
A `found` flag is set to `False`, which we will use to break the `while` loop when `item` has been found. The `while` loop traverses each node in the list until it either runs out of nodes to visit, or `found` changes to `True`. At each node, its data is compared to the item being searched. If the data matches `item`, `found` is changed to `True` thus breaking the loop in the next iteration. Returns a boolean to indicate if `item` was found in the linked list.

## `remove(self, item)`
This implementation of `remove` assumes that the item exists in the list. A robust implementation would need to account for `item` not being found. The method tracks two nodes – `current` and `previous`, as when the node to be removed is found it will need to bridge the gap between that node's previous link and its next link in the list. When `item` is found in the current node, the method points the previous node's link to the current node's next link, thus 'orphaning' the current node and removing it from the linked list.

## `append(self, item)`
Traverses through the list until it reaches the final node. It then creates a new node with `item` as its data, and points the last node in the list to the new `item` node.

## `insert(self, index, item)`
Tracks the current node, the previous node and the index of the current node. It uses a `while` loop to iterate through the nodes until the iteration count matches the value of `index` (a `for` loop would probably be cleaner here). When the value of `index` is reached, a new node is created containing `item` as its data and the current node in the iteration as its `.next` attribute. Finally, the method checks if `previous` has a value. If it doesn't, it means that `previous` is `None` and `current` is the head node. If there is a previous node, it is set to point to the new `item` node. If there isn't, then the new node is set as the head node.

## `index(self, item)`
Tracks the current node and an index value. It iterates through each node in the list until the node whose data matches `item` is found, incrementing the index value with each iteration. When `item` is found, the value of `index` is returned.

## `pop(self)`
Tracks the current node and the previous node. Uses a `while` loop to traverse to the last node in the list. Once at the final node, it performs a check to see if there is a previous node. If a previous node is found its `next` attribute is set to `None`, thus orphaning and removing the final node. If no previous node is found it means that the current node is the first node in the list, so the head of the list is changed to `None` to remove this node. Finally, the data of the current node is returned to the caller.

---
### See also:
- [[What is an unordered list?]]
- [[Operations of an unordered list]]