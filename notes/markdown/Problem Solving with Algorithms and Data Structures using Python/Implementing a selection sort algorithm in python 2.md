Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.8
Date: 2021-11-04

---
# Implementing a selection sort algorithm in python
```python
def selection_sort(collection):
	for pass_num in range(len(collection) - 1):
		max_index = 0
		last_index = len(collection) - pass_num - 1
		for i in range(len(collection) - pass_num):
			if collection[i] > collection[max_index]:
				max_index = i
		collection[last_index], collection[max_index] = collection[max_index], collection[last_index]
```

The first line of the algorithm establishes a loop for sequentially passing through the collection $n-1$ times. Inside each pass, we remember the index position of the highest-value element and calculate the index position at which the highest value element should be placed for that particular pass.

Next we traverse through each unsorted item in the list, and update the value of `max_index` when a new higher value is found. Finally we swap the highest-value element found with whichever element is currently in the `last_index` position.

---
### See also:
- [[What is a selection sort?]]