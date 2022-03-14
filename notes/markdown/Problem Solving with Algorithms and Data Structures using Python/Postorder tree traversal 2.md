Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 7.7
Date: 2021-12-26

---
# Postorder tree traversal
Postorder tree traversal is when a binary tree is traversed by first recursively doing a postorder tree traversal on the left child node, then on the right child node, and then finally visiting the root node.Preorder tree traversal is when a binary tree is traversed by first visiting the root node, then recursively doing a preorder traversal of the left node and then the right node.

```python
def postorder_traversal(tree):
	if tree:
		postorder_traversal(tree.left_child)
		postorder_traversal(tree.right_child)
		print(tree.key)
```

First we check that the tree is not `None`. Next we recursively run the function on the left sub-tree, then the right sub-tree, before finally visiting the root node and printing out its value.

---
### See also:
- [[Preorder tree traversal]]
- [[What is a binary tree?]]
- [[Implementing a binary tree using python]]