---
aliases: [depth first search, depth-first search]
Date: 2022-01-21
---
Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] ch8.15

---
# What is a depth first search?
Like [[What is breadth first search?|breadth first search]] (DFS), depth first search (DFS) is an algorithm for searching [[What is a graph?|graphs]] and graph-like structures (such as trees). Both algorithms will take a starting node/vertex, and build a search tree that spans out from this node at its root. Where they differ is that a BFS algorithm visits all immediate neighbour/child nodes before moving on, thereby building the resulting search tree one level at a time, whereas DFS builds the search tree one branch at a time by recursively visiting the first available neighbour/child node until there are no more available connections to explore, then backtracking its path until it returns to a node that has other unvisited neighbours/children, where the process continues the same way (one branch at a time).

![depth first search](https://raw.githubusercontent.com/nickbalestra/nickbalestra.github.io/master/assets/images/tree-traversal-algos.png)
