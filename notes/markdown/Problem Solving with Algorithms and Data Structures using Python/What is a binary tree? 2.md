---
aliases: [Binary trees, binary tree,]
---
Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 7.5
Date: 2021-12-13

---
# What is a binary tree?
A binary tree is a type of **tree** datatype. A tree is composed of **nodes**, each of which can have zero or more *branches* or *edges* – connections to other **child nodes**. A child node can only exist under a single parent node. Where two or more nodes share the same parent node, they are referred to as **siblings**. At the top of the tree data structure is the **root** node. The root node is the first node of the tree, from which all other nodes emerge.

A binary tree shares all the same properties of a regular tree, but there is a limit on the number of edges that each node can have. At most, each node can be connected to two children.

Some common terms to know when working with trees:

- **Level**: the level of a particular node is the total number of edges that connect it to the root node. Think of it as the distance from the root.
- **Height**: the height of a tree is equal to the level of the node furthest from the root. Think of it as the maximum level of all the tree's nodes. When working with [[Complete binary trees]], the height of the tree can be deducted if the number of nodes $N$ in the tree is known by using the formula $ceil(log_2N)$ ($ceil$ = round up to the nearest integer).