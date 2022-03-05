---
aliases: []
Date: 2022-01-17
---
Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] ch8.9

---
# Implementing breadth first search on a graph
To implement a [[What is breadth first search?|breadth first search]] (**BFS**) algorithm on a [[What is a graph?|graph]], we obviously need `Graph` and `Vertex` classes for the algorithm to interface with. We will use the following classes:

```python
class Vertex:

	def __init__(self, key):
		self.key = key
		self.connected_to = {}
		self.distance = 0
		self.visited = False
		self.fully_searched = False
		self.predecessor = None

	def add_connection(self, to_vertex, weight=0):
		self.connected_to[to_vertex] = weight
		
	def __str__(self):
		return str(self.id) + 'connected to: ' + str([vertex.key for vertex in self.connected_to])
		
	def get_connections(self):
		return self.connected_to.keys()
		
	def get_key(self):
		return self.key
		
	def get_weight(self, to_vertex):
		return self.connected_to[to_vertex]


class Graph

	def __init__(self):
		self.vertices = {}
		self.num_vertices = 0

	def add_vertex(self, key):
		new_vertex = Vertex(key)
		self.vertices[key] = new_vertex
		self.num_vertices += 1
		return new_vertex

	def get_vertex(self, key):
		if key in self.vertices:
			return self.vertices[key]
		else:
			return None

	def __contains__(self, key):
		return key in self.vertices

	def add_edge(self, from_vertex, to_vertex, weight=0):
		if from_vertex not in self.vertices:
			self.add_vertex(from_vertex)
		if to_vertex not in self.vertices:
			self.add_vertex(to_vertex)
		self.vertices[from_vertex].add_connection(self.vertices[to_vertex], weight)

	def get_vertices(self):
		return self.vertices.keys()

	def __iter__(self):
		return iter(self.vertices.values())
```

The `Vertex` class has four important attributes that the BFS algorithm will work with – `self.distance`, `self.visited`, `self.fully_searched`, and `self.predecessor`. `self.distance` is populated by the BFS algorithm to mark how far a vertex is from the vertex where the search was started. `self.visited` is a boolean that is changed to `True` when the algorithm encounters the vertex for the first time. It makes the algorithm aware of vertexes that it has already visited. `self.fully_searched` is another boolean which is flipped to `True` when all the vertex's immediate connections (its neighbours) have been visited. `self.predecessor` points to the previous vertex in the path being established by the BFS algorithm – the point of a BFS algorithm is to find the shortest path to an existing vertex in a graph, given another starting vertex. Setting the `self.predecessor` attribute as the algorithm traverses the graph allows us to trace back the path when the algorithm has finished.

With these attributes explained, we can now implement a breadth first search algorithm as a method of the `Graph` class. Notice that part of the implementation involves a [[What is a queue?|queue]] datatype for tracking the vertices that need to be visited next.

```python
from queue import Queue

class Graph:

	[...]

	def bfs(self, start_vertex):
		start_vertex.distance = 0
		to_search = Queue()
		to_search.enqueue(start_vertex)
		while to_search.size > 0:
			current_vx = to_search.dequeue()
			for neighbour in current_vx.get_connections():
				if not neighbour.visited:
					neighbour.visited = True
					neighbour.distance = current_vx.distance + 1
					neighbour.predecessor = current_vx
					to_search.enqueue(neighbour)
			current_vx.fully_searched = True
```

The `to_search` variable keeps track of the vertices that need to be visited. Each time we enqueue a new vertex to `to_search`, we can be sure that the algorithm will eventually get around to search its neighbouring vertices once it has searched all other nodes ahead in the queue.

Inside the `while` loop, the first thing we do is dequeue the current vertex from `to_search`. We then loop through the current vertex's immediate neighbours. If a neighbouring vertex has not been visited before, we now change its `visted` attribute to `True` and mark its distance as the distance of its predecessor (the vertex currently being searched) plus 1. Next we point its `predecessor` attribute to the current vertex, before enqueuing the newly encountered neighbour to `to_search`. The algorithm's final step is to mark the current vertex as fully searched when all of its neighbours have been touched.

The algorithm will continue looping through until `to_search` reaches a size of 0, enqueueing new vertices when they are encountered and dequeuing them as they are explored.

With the BFS algorithm implemented, we can now define a simple method to traverse the path established by BFS from any touched node back to the origin of the search.

```python
class Graph:

	[...]

	def traverse(self, vertex):
		if not vertex.visited:
			raise VertexNotInPath("The vertex has not been searched")
		while vertex.predecessor is not None:
			print(vertex.key)
			vertex = vertex.predecessor
		print(vertex.key)
```