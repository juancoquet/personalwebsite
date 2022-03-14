---
aliases: [breadth first search, breadth-first search]
Date: 2022-01-17
---
Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 8.9

---
# What is breadth first search?
Breadth first search (**BFS**) is a search algorithm that typically is applied to tree data structures such as [[What is a binary tree?|binary trees]], but can also be applied to any [[What is a graph?|graph]]-like data structure with interconnected nodes. The premise behind a breadth first search algorithm is that a node's immediate neighbours/descendants should *all* be visited before moving on to neighbours/descendants that are further away.

For example, if a breadth first search were executed on a tree beginning at the root node, all nodes on the first level of the tree would be visited, then all nodes on the second level, then third, etc until the final leaf node is reached.

An interesting property of BFS is that it results in a tree structure even if it was applied to a graph. The starting vertex is the root of the tree, and its neighbouring nodes become its children on the first level of the tree. Their neighbours then become the nodes in the second level of the tree, and so on. As the BFS algorithm ripples out through the graph it touches more vertices which become the nodes in the lower levels of the resulting search tree.