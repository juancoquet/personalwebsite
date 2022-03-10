Note type: #litnote
Source: [[📖 Effective Python]] Item 73

---
# Using `heapq`
The `heapq` module comes with functions for easily implementing heap data structures. These can be implemented as standard python `list` objects. The module comes with operations such as `heapify` to turn a list into a heap, `heappush` to add to the heap (and simultaneously sort the heap) and `heappop` to remove the first item of the sorted heap (and heapify the remaining items once again to maintain correct heap order).