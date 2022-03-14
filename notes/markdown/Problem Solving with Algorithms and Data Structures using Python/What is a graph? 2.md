---
aliases: [graph, graphs]
Date: 2022-01-16
---
Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] ch8.2

---
# What is a graph?
A graph is a datatype similar to a tree – it has nodes (also called 'vertices') and edges that connect them, like a tree. Where they differ is that the edges of a graph can be bidirectional (but aren't always) and graphs do not have a top-down structure. Additionally, the edges of a graph can have an associated **weight**, which can be thought of as the cost of moving along a particular edge. When all the edges in a graph are one-way, we call this a **directed graph** or **digraph**.

We can define a graph with the notation $G = (V, E)$, where $V$ is a set of vertices and $E$ is a set of edges that describe relationships between those vertices. Each edge in is a tuple consisting of two vertices $(v1, v2)$, where $v1, v2 \in V$ ($v1$ and $v2$ are members of set $V$). We can also add a third component to each edge, its weight value. A subgraph $s$ is a set of vertices $v$ and edges $e$ where $v \subset V$ and $e \subset E$ ($v$ is a subset of $V$ and $e$ is a subset of $E$).

For example, we could define the following graph:
$$V = \{v0, v1, v2, v3, v4, v5\}$$
$$ E = \{(v0,v1,5), (v1,v2,4), (v2,v3,9), (v3,v4,7), (v4,v0,1), (v0,v5,2), (v5,v4,8), (v3,v5,3), (v5,v2,1)\}$$
Which describes the following layout:
![[graph_example.png]]

With our graph defined, we can now follow a **path** from one vertex to another. We would define a path as $e_1, e_2, ..., e_n$ where $(e_i, e_i+1) \in E$. With a path defined, we can calculate two separate values known as the **unweighted path length** which is the total number of edges in the path, and the **weighted path length** which is the sum of the weights of all the edges in the path. For example, if we were to follow the path that takes us from $v3$ to $v1$, the sequence of vertices we must visit is $(v3, v4, v0, v1)$ along the path $\{(v3,v4,7), (v4,v0,1), (v0,v1,5)\}$ which has an unweighted path length of 3 and a weighted path length of 13.

When working with a directed graph such as the one above, we can encounter a **cycle** which is simply a path that begins at one node and leads back to the same node. For example, the sequence of vertices $(V5, V2, V3, V5)$ is a cycle. A graph without any cycles is called an **acyclic graph**, and a directed graph without any cycles is called a **directed acyclic graph**, or **DAG**.

![you like dags](https://c.tenor.com/uU7vspUbGygAAAAC/snatch-dags.gif)
