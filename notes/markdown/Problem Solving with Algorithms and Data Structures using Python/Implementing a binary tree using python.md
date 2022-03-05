Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 7.5
Date: 2021-12-13

---
# Implementing a binary tree using python
Since a [[What is a binary tree?|binary tree]] is a fractal datatype (every node has the same properties, creating a fractal structure) each node in a binary tree is represented by a `BinaryTree` class.

```python
class BinaryTree:

	def __init__(self, root_obj):
		self.key = root_obj
		self.left_child = None
		self.right_child = None
		
	def insert_left(self, new_node):
		if self.left_child == None:
			self.left_child = BinaryTree(new_node)
		else:
			insert_node = BinaryTree(new_node)
			insert_node.left_child = self.left_child
			self.left_child = insert_node
		
	def insert_right(self, new_node):
		if self.right_child == None:
			self.right_child = BinaryTree(new_node)
		else:
			insert_node = BinaryTree(new_node)
			insert_node.right_child = self.right_child
			self.right_child = insert_node
```

The `__init__` method takes an object as an argument – this can be any datatype, and it is assigned to `self.key`. This is the value that the node holds. It then sets `self.left_child` and `self.right_child` to `None` – these are the edges of the node.

The two insertion methods work the same way. First, they check if a child already exists in the position where we are trying to insert a new node. If a child doesn't exist, the new node is simply assigned as the new child. However, if a child *does* exist, we can't simply overwrite the child node – we must make the existing child the child of the new node we are trying to insert, before insertion.

To use the class we must instantiate a root node, then use the insert methods to add new nodes which will implicitly create new instances of `BinaryTree` for us.