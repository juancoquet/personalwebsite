Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 7.7
Date: 2021-12-26

---
# Preorder tree traversal
Preorder tree traversal is when a binary tree is traversed by first visiting the root node, then recursively doing a preorder traversal of the left node and then the right node.

The code, written as a function to which a binary tree is passed, is as follows:
```python
def preorder_traversal(bin_tree):
	if binary_tree:
		print(binary_tree.key)
		preorder_traversal(binary_tree.left_child)
		preorder_traversal(binary_tree.right_child)
```

First, we check that the binary tree contains root data (a `key` value). If it does contain data, we print its data and then run the function again recursively on the left child and right child. This works because binary trees are fractal data types – when the left and right nodes are visited by the function, exactly the same structure will be found (or `None`, in which case the initial check is `False` and the function returns).

---
### See also:
- [[What is a binary tree?]]
- [[Implementing a binary tree using python]]