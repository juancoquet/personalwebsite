Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.12
Date: 2021-11-29

---
# Implementing a quick sort algorithm using python
To implement a quick sort algorithm, we use two helper functions: `quick_sort_helper`, which takes a start and end point and recursively calls itself, and `parition`, which is responsible for the heavy lifting – it executes all comparisons, places the pivot value into its correct position and returns the split point for the `quick_sort_helper` function to use in the next recursive call.

```python
def quick_sort(collection):
	quick_sort_helper(collection, 0, len(collection) - 1)
 
def quick_sort_helper(collection, start, end):
	if start < end:
		split_point = partition(collection, start, end)
		quick_sort_helper(collection, start, split_point - 1)
		quick_sort_helper(collection, split_point + 1, end)

def partition(collection, start, end):
	pivot_value = collection[start]
	left_mark = start + 1
	right_mark = end
	done = False
		while not done:
			while left_mark <= right_mark and collection[left_mark] <= pivot_value:
				left_mark += 1
			while collection[right_mark] >= pivot_value and right_mark >= left_mark:
				right_mark -= 1
			if right_mark < left_mark:
				done = True
			else:
				collection[left_mark], collection[right_mark] = collection[right_mark], collection[left_mark]
	collection[start], collection[right_mark] = collection[right_mark], collection[start]
	return right_mark
```

---
### See also:
- [[What is a quick sort?]]