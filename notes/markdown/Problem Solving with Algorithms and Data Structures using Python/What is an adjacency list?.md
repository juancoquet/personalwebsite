---
aliases: [adjacency lists, adjacency list]
Date: 2022-01-17
---
Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] ch8.5

---
# What is an adjacency list?
An adjacency list is a way of representing and implementing a [[What is a graph?|graph]] that is more space-efficient than an [[What is an adjacency matrix?|adjacency matrix]].

In an adjacency list implementation, the graph object holds a master list of all existing vertices and each vertex object holds its own local collection of all other vertices that it is connected to. A good datatype to use for this collection is a dictionary as we can set the keys to be the vertices and set the values to be the weight of the edge that leads to that particular vertex.

![adjacency list](https://runestone.academy/ns/books/published/pythonds/_images/adjlist.png)

This is more space-efficient because no data needs to be stored for non-existing edges, unlike in an adjacency matrix where all possible edges need to be represented to maintain the properties of the matrix.