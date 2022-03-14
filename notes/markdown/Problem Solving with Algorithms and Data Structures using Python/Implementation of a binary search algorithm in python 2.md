Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.4
Date: 2021-11-01

---
# Implementation of a binary search algorithm in python
A binary search algorithm is a good candidate for a recursive implementation as the same sequence of steps must be executed on an ever-dwindling collection of items until either a match is found or no items remain.

The recursive implementation is as follows:

```python
def binary_search(list, item):
	if not list:
		return False
	else:
		midpoint_idx = len(list) // 2
	if list[midpoint_idx] == item:
		return True
	else:
		if list[midpoint_idx] > item:
			return binary_search(list[:midpoint_idx], item)
		else:
			return binary_search(list[midpoint_idx+1:], item)
```

The first step is to check the base case – is the list empty? If the list is empty, then the recursive binary search has dismissed all items in the collection as non-matches, and `False` is returned.

If the collection yet has members, we must identify the midpoint of the list to execute a comparison. We use integer division `//` to acquire an index value for the midpoint of the list. If the list has a odd number of items, this line calculates the index value of the middle item. If the list has an even number of items, this line calculates the index value of the item right-of-center, as there is no true center item. In the case where the length of the list is 1, the calculated index value is 0, or the first (and only) item in the list.

Once we have our index value for the midpoint of the list calculated, we can perform a comparison between the item in the middle of the list and the item being searched for. If the items match, `True` is returned to the caller. If the two items are not a match, further comparisons are needed.

If the midpoint item is greater than the item being searched for, we can dismiss the entire second half of the collection as all its members are also greater than the search item given that the collection is ordered. We use indexing syntax `[start:end]` to call the binary search function again on all items from the start of the list up to the midpoint index (exclusive).

If the midpoint item is less than the item being searched for, we can dismiss the entire first half of the collection as all its members are also less than the search item given that the list is ordered. We use indexing syntax to call the binary search function again on all items from the right of the midpoint (inclusive) to the end of the list.

The function then follows the same sequence of steps on the remaining half of the list – return `False` if the list is empty, calculate the midpoint, return `True` if the midpoint item is a match, or recursively call itself again if no match is found. Eventually either the collection will run out of items through iterative elimination or the midpoint item will return a match. When this happens, either `False` or `True` will be returned to each of the callers in the call [[What is a stack?|stack]], thus completing the recursive function.

---
### See also:
- [[What is a binary search?]]
- [[The three characteristics of recursive algorithms]]