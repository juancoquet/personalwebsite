---
aliases: [Binary heaps, binary heap]
Date: 2021-12-27
---
Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 7.8

---
# What is a binary heap?
A binary heap is a data structure that acts much like a [[What is a queue?|queue]] – items can be added to the queue and when an item is removed from the heap, it is removed from the front. Where it differs is that in a heap, the order in which the items were added will not necessarily persist. Instead, a binary heap will move an item to the top of the heap (the front of the queue) based on its value.

For example, a min heap will always keep the smallest item in the heap at the top, ready to be dequeued next. When that item is removed from the heap, the next-smallest item takes its place at the top of the heap regardless of where it was positioned prior to the removal – a min heap must always keep the smallest member at the top.

Although a binary heap is best conceptualised and diagramed as a [[What is a binary tree?|binary tree]] structure, it is typically implemented using a list.

---
### See also
- [[What is a queue?]]
- [[What is a binary tree?]]
- [[Using `heapq`]]