Note type: #litnote
Source: [[📖 Effective Python]] item 71

---
# Using `deque` for FIFO structures
Python's standard `list` type can be, and often is used, for FIFO data structures. The list queue is simply added to using `.append()` and dequeued from by using `.pop(0)`. The problem with this approach comes when handling large amounts of data, as the `pop` function scales quadratically—first the item at index `0` is popped from the list, then all other items are re-indexed to account for the now missing item such that the front of the list remains index `0`.

Instead, you can use `deque` (*double-ended queue*) from the `collections` module to improve runtime. Using a `deque` object as a queue, the `popleft()` method can be called to pop the next item in the list—this method call scales linearly, meaning much better runtime as data sizes increase.