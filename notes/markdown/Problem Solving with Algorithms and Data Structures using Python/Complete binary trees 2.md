---
aliases: [complete binary tree,]
Date: 2021-12-28
---
Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 7.10

---
# Complete binary trees
A binary tree is considered **complete** when each level of the tree has all its possible nodes (with the exception of the lower-most level). In other words, the current level of the tree must be completely populated before moving on to the next level. This means that the only level of the tree that can be incomplete is the lowest level, where the leaf nodes currently reside.

Using a complete binary tree structure ensures that a binary tree remains **balanced**, meaning that the left and right branches of the root node contain roughly the same number of nodes. Having a balanced binary tree is useful for algorithmic efficiency when implementing a tree in a data structure such as a [[What is a binary heap?|binary heap]].

![image](https://runestone.academy/runestone/books/published/pythonds/_images/compTree.png)

---
### See also:
- [[What is a binary tree?]]
- [[Implementing a binary tree using python]]