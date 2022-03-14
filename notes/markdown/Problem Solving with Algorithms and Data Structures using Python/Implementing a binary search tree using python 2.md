---
aliases: []
Date: 2021-12-29
---
Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 7.13

---
# Implementing a binary search tree using python
A [[What is a binary search tree?|binary search tree]] is implemented through the use of two separate classes – a `BinarySearchTree` class and a `TreeNode` class. It is implemented this way because we need to be able to handle cases where the binary search tree is empty (a regular [[What is a binary tree?|binary tree]] always needs a root object passed to the constructor).

## TreeNode class
```python
class TreeNode:

	def __init__(self, key, value, left_child=None, right_child=None, parent=None):
	self.key = key
	self.value = value
	self.left_child = left_child
	self.right_child = right_child
	self.parent = parent
```

The `TreeNode` class represents a node within the binary search tree. The `key` property is used for making comparisons, while the `value` property is the data we are interested in storing. For simple data types, like `int`, these two can be the same thing. However, for more complex datatypes like custom class instances, we can provide a specific key to use for comparisons.

As an example, if we have a `Person` class with `last_name`, `first_name` and `date_of_birth` properties, we can choose any of these properties to make comparisons by providing it to the `key` parameter during the initiation of the `TreeNode` object. We can do something like `TreeNode(key=person_obj.last_name, value=person_obj)` which will create a node out our person object and our binary search tree will use the `last_name` property to make comparisons to other objects within the tree for sorting purposes.

the child and parent properties will point to other instances of `TreeNode` in our binary search tree. They can also point to `None`, when the node in question is a leaf node or root node respectively.

```python
class TreeNode:

	[...]

	def is_left_child(self):
		return self.parent and self.parent.left_child == self

	def is_right_child(self):
		return self.parent and self.parent.right_child == self
```

The `is_left_child` method checks to see if the node has a parent, and if the parent's left child  is `self`, the node making the call. Returns `True` if both conditions are met, indicating that the node in question exists as the left child of another node. The `is_right_child` performs the same operations but checks if the node is the right child of another node.

```python
class TreeNode:

	[...]

	def is_root(self):
		return not self.parent
	
	def is_leaf(self):
		return not (self.left_child or self.right_child)
	
	def has_any_children(self):
		return self.left_child or self.right_child
	
	def has_both_children(self):
		return self.left_child and self.right_child
```

These methods are somewhat similar in operation to the `is_left_child` method described above – they simply check the condition described in the method name by looking at surrounding nodes (if any).

```python
class TreeNode:

	[...]

	def update_left_child(self, new_node):
		self.left_child = new_node
		if new_node:
			new_node.parent = self
	
	def update_right_child(self, new_node):
		self.right_child = new_node
		if new_node:
			new_node.parent = self
```

`update_left_child` first overwrites whatever node is in the calling node's `left_child` property. Then, if the newly added node is not `None` (indicating that it is an instance of `TreeNode`), it sets the `parent` property of the replacement node to the `TreeNode` object calling the method. `update_right_child` does the same thing but for updating the right child.

```python
class TreeNode:

	[...]

	def replace_node_data(self, key, value, left_child, right_child):
		self.key = key
		self.value = value
		self.left_child = left_child
		self.right_child = right_child
		if self.has_left_child():
			self.left_child.parent = self
		if self.has_right_child():
			self.right_child.parent = self
```

`replace_node_data` replaces all the calling object's data with the provided values.

```python
class TreeNode:
	
	[...]

	def __iter__(self):
		if self:
			if self.has_left_child():
				for node in self.left_child:
					yield node
			yield self
			if self.has_right_child():
				for node in self.right_child:
					yield node
```

The `__iter__` method allows for [[Inorder tree traversal]] through the binary search tree. It is particularly interesting because it is deceptively recursive, as the `__iter__` dunder method is implicitly called whenever the `for` keyword is used.

The method begins by checking that `self` is not `None`. It then proceeds to check for the existence of a left child – if a left child exists, a for loop is called on the left child. Here is where the recursion happens, because python will implicitly call the left child's `__iter__` method. This recursive step will continue down the left branch until the left-most node is reached.

When the left-most node is reached its left child will also be checked, which will be `None`. At this point, the left child check fails and the method proceeds to `yield self`, yielding the left-most node in the tree. Next, the same recursive process is followed on the right child.

```python
class TreeNode:

	[...]

	def splice_out(self):
		if self.is_leaf():
			if self.is_left_child():
				self.parent.left_child = None
			else:
				self.parent.right_child = None
		elif self.has_any_children():
			if self.has_left_child():
				if self.is_left_child(): # has left child and is left child
					self.parent.left_child = self.left_child
				else: # has left child and is right child
					self.parent.right_child= self.left_child
				self.left_child.parent = self.parent
			else: # has right child
				if self.is_left_child(): # has right child and is left child
					self.parent.left_child = self.right_child
				else: # has right child and is right child
					self.parent.right_child = self.right_child
				self.right_child.parent = self.parent
```

`splice_out` orphans the caller node and points any child/parent nodes to where they belong once it's absent from the tree. This method is used internally to remove a **successor** 
 node, so it only handles the removal of a node with zero or one child. ![[Implementing a binary search tree using python#^a2bc10]]
 
The first step is to check if the caller node is a leaf node. If it's a leaf node, orphaning it is quite easy as there are no children that need to be pointed to a new parent – the only thing that needs to be done is check if the caller node is a left child or a right child, and point the parent's appropriate child property to `None` to successfully remove the caller node from the tree.

If the caller node has a child, we check which side the child is on. In order for the child node to take the caller node's place in the tree, we need to know which side of the parent the caller node connects to, which we check by making use of the `is_left_child` and `is_right_child` methods created earlier.

There are four possible scenarios if the caller node has a child – it has a left child and is (itself) the left child of its parent, it has a left child and is the right child of its parent, it has a right child and is the left child of its parent, or it has a right child and is the right child of its parent. Knowing both of the caller node's connections the the level above and the level below in the tree allows us to connect its child node to the correct side of its parent node, allowing us to safely orphan the caller node without orphaning its child.

```python
class TreeNode:

	[...]

	def find_successor(self):
		successor = None
		if self.has_right_child():
			successor = self.right_child.find_min()
		else:
			if self.parent:
				if self.is_left_child():
					successor = self.parent
				else: # is right child
					self.parent.right_child = None
					successor = self.parent.find_successor()
					self.parent.right_child = self
		return successor
	  
	def find_min(self):
		current_node = self
		while current_node.has_left_child():
			current_node = current_node.left_child
		return current_node
```

The final two methods of `TreeNode` are `find_successor` and `find_min`. The latter is a helper method called by the former. `find_min` simply fetches the smallest member of a subtree given a starting node, by repeatedly following the left branch of every node it encounters until it reaches a `None` value, thereby finding the left-most node in the binary search sub-tree which is always the smallest member.

The **successor** of a node is another node that can take its place without violating the binary search tree properties. ^a2bc10

We can find the successor of a node by locating the node with the next-largest key in the tree, which is what `find_successor` does. First we check if the caller node has a right child. If it does, every member of the right child sub-tree is greater than the calling node, so we use `find_min` to find the smallest node within this tree, thereby giving us the successor of the caller node which will be the left-most node of its right sub-tree.

If the caller node doesn't have a right child, the successor must be found elsewhere, higher up in the tree. If the caller node is a left child, then the successor is its parent (which is of course greater than the caller node, being the parent's left child). To illustrate this point with some examples – any right child of the parent would be bigger than the parent, therefore not the next-largest node; if the parent itself is a left child of another node then the parent's parent is larger than the parent, therefore not the next-largest node; if the parent is a right child then the parent's parent is smaller than the caller node, as the caller node exists in the parent's parent's right sub-tree. We can leverage the properties of a binary search tree to eliminate all nodes other than the direct parent.

If the caller node is a right child, it's a little more complex. First we detach the caller node (along with its sub-tree) from the tree in order to remove these nodes from consideration during the next step, where we find the parent node's successor using a recursive call. Since the parent node now (temporarily) doesn't have a right child, the first section of the control flow (`if self.has_right_child()`) will not be applicable so the algorithm aims to find a successor higher up in the tree – it will check if the parent is a left child, returning the parent's parent as the successor if that's the case, or it will continue making recursive calls until either a successor is found or the root node is reached. The root node is reached when the `if self.parent` check fails, meaning that no valid successor exists as there is no node present in the tree that is greater than the original caller node – in this case `None` is returned up the call [[What is a stack?|stack]] instead of a successor node.

When a successor is found (or when the root is reached), each call in the call [[What is a stack?|stack]] puts back the right child sub-tree that it removed during prior recursive calls, reverting the tree to its original state.

## BinarySearchTree Class
```python
class BinarySearchTree:

	def __init__(self):
		self.root = None
		self.size = 0
	
	def __len__(self):
		return self.size
```

The `BinarySearchTree` class represents a network of `TreeNode` objects. `self.root` points to the root node, acting as an entry point into the tree structure where all other nodes can be accessed from.

```python
class BinarySearchTree:

	[...]

	def put(self, key, value):
		if self.root:
			self._put(key, value, self.root)
		else:
			self.root = TreeNode(key, value)
			self.size += 1
	
	def _put(self, key, value, current_node):
		if key < current_node.key: # left branch
			if current_node.left_child:
				self._put(key, value, current_node.left_child)
			else:
				current_node.left_child = TreeNode(key, value, parent=current_node)
		else: # right branch
			if current_node.right_child:
				self._put(key, value, current_node.right_child)
			else:
				current_node.right_child = TreeNode(key, value, parent=current_node)

	def __setitem__(self, key, value):
		self.put(key, value)
```

There are three methods involved in inserting a new node into the tree. Of these, the `_put` internal method does all the heavy lifting. It takes three parameters – a key, a value, and a current node. When `_put` is first called, it is passed the root node to its `current_node` parameter. It then begins by comparing the provided key argument to the current node's key to identify which branch of the tree the new item belongs in.

If the new node belongs in the left branch, it checks the current node's left child to see if it is already populated. If it is, a recursive call is made, this time proving the left child as the `current_node` argument. If the left child is not occupied, then the new value can be inserted as the current node's left child by creating a `TreeNode` instance with the `key` and `value` arguments, and setting its parent to the current node. The same process occurs if the new node belongs in the right branch of the tree.

The `_put` method will recursively call itself, following different branches of the tree with each comparison, until an appropriate place for the new node is found.

The `put` method exists as a layer of abstraction above the `_put` method – first, it checks for the existence of a root node in the tree. If a root node exists it calls `_put`, providing the root as the `current_node` argument. If no root node exists, a root node is created using the `key` and `value` arguments provided.

Finally, the `__get__` dunder method allows the user to use dictionary-like syntax to insert new nodes. It will implicitly call `put` with the provided values when the syntax `bin_tree['key'] = 'value'` is used, where `bin_tree` is an instance of `BinarySearchTree`.

```python
class BinarySearchTree:

	[...]

	def get(self, key):
		if self.root:
			result = self._get(key, self.root)
			if result:
				return result.value
			else:
				return None
		else:
			return None
	
	def _get(self, key, current_node):
		if not current_node:
			return None
		elif current_node.key == key:
			return current_node
		elif key < current_node.key:
			return self._get(key, current_node.left_child)
		else:
			return self._get(key, current_node.right_child)

	def __getitem__(self, key):
		return self.get(key)

	def __contains__(self, key):
		if self._get(key, self.root):
			return True
		else:
			return False
```

Retrieving an item follows a similar procedure to inserting a new item. There are once again three 'getter' methods, and an extra `__contains__` method to check for the existence of a node.

Like `_put`, the heavy lifting in retrieving a node is done recursively by `_get`. It is provided two arguments – a key to search for and a node to begin operating on. The first step is to check that the current node is not `None`, as this would mean that the key has not been found in the tree. Next we check if the current node's key is the key being searched for. If it is, the current node is returned. If it isn't we proceed to make a comparison to the current node's key in order to decide which branch of the tree to continue the search on.

If the key being searched for is less than the current node's key, `_get` calls itself recursively on the current node's left child. If it's greater than the current node's key, the process follows on the current node's right child. The `_get` method will continue to make recursive calls until it either finds a matching key, in which case it will return the node where the matching key was found, or until it is passed `None` as the current node, meaning that a leaf node was reached and still no match was found.

The `_get` internal method is called by `get`, which first checks for the existence of a root node. If a root node exists, it begins the recursive `_get` process from the root and returns the result found (or `None`).

The two dunder methods allow the user to use python dictionary-like syntax for retrieving nodes and checking for the existence of keys within the tree. `__getitem__` allows for syntax like `found_node = bin_tree['key']`, while `__contains__` allows for the use of the `in` python keyword, like `'key' in bin_tree` which evaluates to `True` or `False`.

```python
class BinarySearchTree:

	[...]

	def __iter__(self):
		return self.root.__iter__()
```

The `__iter__` dunder method allows for [[Inorder tree traversal]]. It calls the root node's `__iter__` method, which is described above.

```python
class BinarySearchTree:

	[...]
	
	def delete(self, key):
		if self.size > 1:
			node_to_remove = self._get(key, self.root)
			if node_to_remove:
				self.remove(node_to_remove)
				self.size -= 1
			else:
				raise KeyError('Error, key not in tree')
		elif self.size == 1 and self.root.key == key:
			self.root = None
			self.size -= 1
		else:
			raise KeyError('Error, key not in tree')
	
	def __delitem__(self, key):
		self.delete(key)
```

The most complex methods of the `BinarySearchTree` class handle the deletion of a node. It's a complex procedure because we need to make sure that no parts of the tree are orphaned in the deletion process, and any changes we make to the tree need to maintain the binary search tree properties.

The `delete` method itself is fairly simple. The complexity is handled by the `remove` method, which is called within.

There are two discrete cases that need to be handled – where the tree has more than one node, and when the tree consists of only a root node. This is because in a tree with more than one node, a node is removed by changing the surrounding node's children and parent  attributes, whereas when we are only working with a root node we only need to set `self.root` to `None` to delete it.

The `delete` method first checks if the size of the tree is greater than 1. If so, it tries to find the node node related to the provided `key` argument by using the previously defined `_get` internal method.  If a matching node is found, it calls `remove` on this node which removes the node and rearranges the tree around it (this process is described in detail below).

If the tree size is not greater than one, that means we are dealing with just a root node. We check to make sure that the root node matches the key we wish to delete, and set the root node to `None` if that is the case.

The `__delitem__`  dunder method allows for the use of the `del` python keyword like, and it calls the `delete` function.

```python
class BinarySearchTree:

	[...]
	
	def remove(self, current_node):
		if current_node.is_leaf(): # current_node has no children
			if current_node == current_node.parent.left_child:
				current_node.parent.left_child = None
			else:
				current_node.parent.right_child = None
		elif current_node.has_both_children():
			successor = current_node.find_successor()
			successor.splice_out()
			current_node.key = successor.key
			current_node.value = successor.value
		else: # current_node has one child
			if current_node.has_left_child(): # current_node only has left child
				if current_node.is_left_child():
					current_node.left_child.parent = current_node.parent
					current_node.parent.left_child = current_node.left_child
				elif current_node.is_right_child():
					current_node.right_child.parent = current_node.parent
					current_node.parent.right_child = current_node.right_child
				else: # current_node is root
					current_node.replace_node_data(
						key=current_node.left_child.key,
						value=current_node.left_child.value,
						left_child=current_node.left_child.left_child,
						right_child=current_node.left_child.right_child
					)
			else: # current_node only has right child
				if current_node.is_left_child():
					current_node.right_child.parent = current_node.parent
					current_node.parent.left_child = current_node.right_child
				elif current_node.is_right_child():
					current_node.right_child.parent = current_node.parent
					current_node.parent.right_child = current_node.right_child
				else: # current_node is root
					current_node.replace_node_data(
						key=current_node.right_child.key,
						value=current_node.right_child.value,
						left_child=current_node.right_child.left_child,
						right_child=current_node.right_child.right_child
					)
```

Finally, the `remove` method is by far the most complex algorithm in the `BinarySearchTree` class, as it incorporates many nested clauses to successfully maintain the binary search tree properties.

There are four separate cases to handle:
	1. The node being removed is a leaf node (no children)
	2. The node being removed has both children
	3. The node being removed only has a left child
	4. The node being removed only has a right child

The first case is the simplest – we begin by checking if the current node (passed to it as an argument by the `delete` method) is a leaf node. If so, we check whether it's a left or right child, and update the corresponding parent's left or right child property to `None` to successfully remove the node.

The second case, where two children are present, requires us to find a successor to replace the node we are removing. When a successor is found, it is spliced out of the tree and the current node is overwritten with the successor's key and value.

The third and the fourth case are handled the same way. Here we will describe the removal a node with a right child (case number 4). In order to proceed, we need to know if the current node itself is a left child, a right child, or neither (indicating that it's the root node). 

If it's a left child, we must point its parent's left child attribute (which presently points to the current node) to the current node's right child, and we must also point the right child's parent attribute to the current node's parent. This allows us to successfully 'bypass' the current node, thus orphaning it from the rest of the tree.

If the current node is a right child, a similar procedure is followed except we bypass it by pointing the parent's right child attribute to the current node's right child.

Finally, if the current node is neither a left child or a right child, that means that it's the root node. In this case we simply overwrite the node using `replace_node_data` as there are no other dependent nodes to take care of.