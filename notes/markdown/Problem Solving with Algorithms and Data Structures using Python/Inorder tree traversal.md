Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 7.7
Date: 2021-12-26

---
# Inorder tree traversal
Inorder tree traversal is when a binary tree is traversed by first recursively doing an inorder traversal of the left child node, then visiting the root node before finally doing an inorder traversal on the right child node.

```python
def inorder_traversal(tree):
	if tree:
		inorder_traversal(tree.left_child)
		print(tree.key)
		inorder_traversal(tree.right_child)
```

First we check that the tree is not `None`, then we execute our recursive calls and visit the root node.

---
### See also:
- [[Postorder tree traversal]]
- [[Preorder tree traversal]]
- [[What is a binary tree?]]
- [[Implementing a binary tree using python]]