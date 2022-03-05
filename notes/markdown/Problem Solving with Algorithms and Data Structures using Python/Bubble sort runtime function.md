Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.7
Date: 2021-11-04

---
# Bubble sort runtime function
Since the bubble sort algorithm relies on a nested loop to traverse each item in the list multiple times, the runtime function is $O(n^2)$. However, bubble sort has an advantage in cases where the list becomes sorted early. Due to its property of complete traversal of a list, the algorithm can be modified to detect when no swaps have occurred on a particular pass which means that all items are in order, and the algorithm can be cut short.

---
### See also:
- [[What is a bubble sort?]]
- [[Implementing a bubble sort algorithm in python]]