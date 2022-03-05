---
aliases: []
Date: 2022-01-17
---
Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] ch8.6

---
# Implementing a graph using python
The following code shows a [[What is a graph?|graph]] implementation using an [[What is an adjacency list?|adjacency list]]. It is composed of two classes – `Vertex`, which represents the vertices in the graph and their properties, and `Graph`, which holds the instances of `Vertex` and provides an interface to the overall data structure.

```python
class Vertex:

	def __init__(self, key):
		self.key = key
		self.connected_to = {}

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
```

The constructor method takes a `key` argument which serves as a name or ID for the vertex, usually a string. It also initialises an empty dictionary which will keep track of other vertices it is connected to with the format `{vertex: weight}`.

The `add_connection` method adds a new edge from the current vertex to another. It takes `to_vertex`, a `Vertex` object, and `weight` as arguments. The `get_weight` method returns the weight of the edge to the target vertex.

```python
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

The constructor method for the `Graph` class keeps a `self.vertices` dictionary which maps `Vertex`  keys to `Vertex` objects, for example `{v1.key: v1, v2.key: v2}`. All the vertices that exist in the graph are stored in this dictionary.

The `add_vertex` method takes a `key` argument and creates a new `Vertex` object with the given key, then adds the key/object pairing to `self.vertices`.

The `add_edge` method takes three arguments. `from_vertex` and `to_vertex` are both vertex keys, while weight is an `int`. If either of the two keys provided don't exist within `self.vertices`, new `Vertex` objects will be created and added before proceeding. The last line takes the provided keys and indexes into `self.vertices`, accessing the `Vertex` object to which each key points and adds an edge between them by using the `from_vertex` object's `add_connection` method defined above.

Finally, `get_vertices` allows us to see all the keys in `self.vertices` while the `__iter__` method allows us to loop through the `self.vertices` values, the actual vertex objects themselves.