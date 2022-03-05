Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 7.10
Date: 2021-12-28

---
# Implementing a binary heap using python
We will be [[implementing a binary heap using a list]]. The [[What is a binary heap?|binary heap]] implementation is as follows:

```python
class BinaryHeap:
	def __init__(self):
		self.heap_list = [0]
		self.current_size = 0
	
	def percolate_up(self, i):
		while i // 2 > 0:
			if self.heap_list[i] < self.heap_list[i // 2]:
				self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
			i = i // 2

	def insert(self, value):
		self.heap_list.append(value)
		self.current_size += 1
		self.percolate_up(self.current_size)

	def percolate_down(self, i):
		while (i * 2) <= self.current_size:
			min_child_idx = self.min_child(i)
			if self.heap_list[i] > self.heap_list[min_child_idx]:
				self.heap_list[i], self.heap_list[min_child_idx] = self.heap_list[min_child_idx], self.heap_list[i]
			i = min_child_idx

	def min_child(self, i):
		if i * 2 + 1 > self.current_size:
			return i * 2
		else:
			if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
			return i * 2
		else:
			return i * 2 + 1

	def extract_min(self):
		min_val = self.heap_list[1]
		self.heap_list[1] = self.heap_list[self.current_size]
		self.current_size -= 1
		self.heap_list.pop()
		self.percolate_down(1)
		return min_val

	def heapify(self, arr):
		i = len(arr) // 2
		self.current_size = len(arr)
		self.heap_list = [0] + arr[:]
		while i > 0:
			self.percolate_down(i)
			i -= 1
```

- `percolate_up` is used as a helper function, it takes the index value of an item in the heap. It compares the item at the given index with its parent node and swaps their positions in the heap if the parent node's value is greater than the value at the given index. It makes these comparisons sequentially all the way back to the root node, each time making a swap if necessary. It is only called by `insert`, which provides it with the last index value in the heap.
- `insert` takes a value and inserts it in its proper place in the heap by calling `percolate_up` as a helper function.
- `percolate_down` is a helper that does the opposite of `percolate_up` – it takes the item at the top of the heap and compares it to the lesser of its two children (where two children are present). If the smaller of the two children is smaller yet than the root node, they are swapped. The comparisons are sequentially executed all the way to the lowest level of the tree, each time making a swap if necessary. It is called by `extract_min` and `heapify` as a helper function to maintain heap properties when the smallest heap item is removed and when a new heap is being created.
- `min_child` is a helper to `percolate_down` – it takes the index of a node in the heap, and returns the index of the lesser of its two children.
- `extract_min` moves the last item in the heap to the top, then calls `percolate_down` to maintain heap properties before returning the value that was previously at the top of the heap, the smallest member.
- `heapify` generates a heap from an unordered list. It makes calls to `percolate_down` starting from the midpoint of the array as, given the properties of a binary tree structure, every item after this point is a leaf node and cannot be moved further down the heap. It works its way back from the midpoint to the root node, each time calling `percolate_down` to have a fully built heap by the end.

---
### See also:
- [[Operations of a binary heap]]
- [[What is a binary heap?]]
- [[How a heap is ordered]]
- [[Using `heapq`]]
- [[What is a binary tree?]]
- [[Complete binary trees]]