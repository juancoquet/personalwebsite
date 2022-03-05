Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.3
Date: 2021-11-01

---
# Implementing a sequential search algorithm in python
The code for a sequential search is straight forward. We loop through a collection using and compare each item to the item being searched for. If a match is found, we return `True` thus escaping the loop. If no match is found and we run out of items to traverse, we return `False`.

```python
def sequential_search(list, item):
	for i in list:
		if i == item:
		return True
	return False
```

This implementation assumes that the list is unordered. When dealing with an ordered list, we can compare the value of each item and decrease runtime cost as in many cases we would not have to traverse the entire list to know that the item being searched is not a member.

---
### See also:
- [[What is sequential search?]]
- [[Operations of an ordered list]]