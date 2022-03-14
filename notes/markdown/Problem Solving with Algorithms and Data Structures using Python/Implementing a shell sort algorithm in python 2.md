Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.10
Date: 2021-11-14

---
# Implementing a shell sort algorithm in python
The shell sort algorithm requires a helper function that runs an insertion sort on a sub-list of items that are spaced $s$ positions apart. We call this function `gap_insertion_sort`, and it takes three arguments – the original collection being sorted, a start point, and a gap distance ($s$).

```python
def shell_sort(collection):
	sublist_count = len(collection) // 2
	while sublist_count > 0:
		for start_position in range(sublist_count):
			gap_insertion_sort(collection, start_position, sublist_count)
		sublist_count = sublist_count // 2

def gap_insertion_sort(collection, start, gap):
	for i in range(start+gap, len(collection), gap):
		current_value = colleciton[i]
		position = i
		while position >= gap and collection[position-gap] > current_value:
			collection[position] = collection[position-gap]
			position -= gap
		collection[position] = current_value
```

The `gap_insertion_sort` function starts by establishing a loop that iterates over index values beginning with at the second item in the sub-list. This item is compared to the first item in the sub-list and swapped if necessary, before considering the next (third) item in the sub-list and repeating the process of comparing and swapping positions with previous items if necessary – this is just like the a standard insertion sort with the exception that there is a gap of distance $s$ between the sub-list's items. The `gap_insertion_sort` algorithm ends when the last item in the sub-list has been considered and compared against its predecessors.

The `shell_sort` algorithm that calls `gap_insertion_sort` is responsible for creating the sub-lists, making the number of sub-lists $s$ smaller but containing more items with each iteration. By the time we get to the final `gap_insertion_sort` call where $s=1$, all the items in the overall collection are close to being fully sorted so not many changes are necessary.

---
### See also:
- [[What is a shell sort?]]
- [[What is an insertion sort?]]
- [[Implementing an insertion sort algorithm in python]]