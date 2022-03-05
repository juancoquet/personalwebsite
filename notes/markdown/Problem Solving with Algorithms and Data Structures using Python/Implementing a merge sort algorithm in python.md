Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.11
Date: 2021-11-15

---
# Implementing a merge sort algorithm in python
The first step for a recursive algorithm is to check the base case. In the case of merge sort, the base case is reached when a sub-list has a length of 1. If the length of the list is greater than 1, we continue to split the list into two halves. If the length isn't greater than one, then no splitting or sorting needs to be done and the caller can continue with the rest of the algorithm, which compares and merges each sub-list's values.

```python
def merge_sort(collection):
	if len(collection) > 1:
		midpoint = len(collection) // 2
		left_half = collection[:midpoint]
		right_half = collection[midpoint:]
		
		merge_sort(left_half)
		merge_sort(right_half)
		
		idx_left = 0
		idx_right = 0
		idx = 0
		while idx_left < len(left_half) and idx_right < len(right_half):
			if left_half[idx_left] <= right_half[idx_right]:
				collection[idx] = left_half[idx_left]
				idx_left += 1
			else:
				collection[idx] = right_half[idx_right]
				idx_right += 1
			idx += 1
			
		while idx_left < len(left_half):
			collection[idx] = left_half[left_idx]
			left_idx += 1
			idx += 1
			
		while idx_right < len(right_half):
			collection[idx] = right_half[right_idx]
			right_idx += 1
			idx += 1
```

The merging process utilises three index values – one for the left half of the list, one for the right half, and one for the master list, into which the sorted items are inserted in-place.

The first `while` loop iterates until either the left half or right half's items have all been placed into the composite list. With each iteration, the lesser value's corresponding list's index is incremented so that the next value in the list is used for comparison in the next iteration. The master list index value is also incremented after the value has been placed so that the next item is placed into the next position.

Once one of the list's items have all been placed, another `while` loop is used to insert all remaining items in the other list into the master list in the order in which they appear, as they are already sorted. The merging process propagates up the call [[What is a stack?|stack]] until the last two ordered sub-lists are merged into the final ordered master list.

---
### See also:
- [[What is a merge sort?]]
- [[The three characteristics of recursive algorithms]]