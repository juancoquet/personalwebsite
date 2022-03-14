---
aliases: [spanning tree]
Date: 2022-01-26
---
Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 8.22

---
# What is a spanning tree?
A spanning tree is an acyclic subset of the edges of a [[What is a graph?|graph]] that connects every vertex. In other words, it is a [[What is a strongly connected component?|strongly connected component]] that links every vertex in a graph. Moreover, we can choose to optimise a spanning tree to turn it into a **minimum weight** spanning tree – this would be a spanning tree whose total weight of all its edges adds up to the minimum possible value.

Below is an example of a minimum weight spanning tree overlaid on the graph to which it pertains. The spanning tree is represented by solid lines, while the entire graph is represented by both solid lines and dotted lines (the dotted lines are edges that form part of the graph but don't form part of the minimum weight spanning tree).

![min weight spanning tree](https://runestone.academy/ns/books/published/pythonds/_images/mst1.png)
