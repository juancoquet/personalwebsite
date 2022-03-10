Note type: #litnote
Source: [[📖 Python Cookbook]] ch1.3 p6

---
# Using deque to keep fixed-length arrays of the previous N items
Deque objects can be used to keep a list of the last N items processed in a loop by providing a `maxlen` argument when instantiating the object.
```python
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)	# [1, 2, 3]

q.append(4)
print(q)	# [2, 3, 4]

q.append(5)
print(q)	# [3, 4, 5]
```

The same can be done manually, e.g. with slicing, but using a deque object is both cleaner and runs a lot faster—adding or popping items from either end of a deque object always has O(1) complexity, whereas inserting or removing items from a list has a complexity of O(N).