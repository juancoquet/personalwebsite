Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 7.9
Date: 2021-12-27

---
# Operations of a binary heap
A binary heap typically has the following operations:
- **Heapify**: process to rearrange a collection of items into a heap structure(min/max item at the top of the heap).
- **Percolate up**: process to position a new item added to the heap in its proper place.
- **Insert**: adds a new item to the heap. Calls the above percolate method to maintain heap properties.
- **Find max/min**: returns the value at the top of the heap, i.e. the min or max value depending on the type of heap.
- **Extract max/min**: returns and removes the value at the top of the heap. 

---
### See also:
- [[What is a binary heap?]]
- [[Using `heapq`]]