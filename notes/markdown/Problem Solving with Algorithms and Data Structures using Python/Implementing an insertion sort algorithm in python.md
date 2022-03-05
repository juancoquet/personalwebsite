Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.9
Date: 2021-11-12

---
# Implementing an insertion sort algorithm in python
To implement an insertion sort algorithm in python, we begin by looping through each index in the collection, but skipping the first item (i.e. starting at index 1). We then establish a variable to 'remember' the value found at the index currently being considered so that we can overwrite this index position in subsequent steps.

Next we use a `while` loop to compare the value being considered to all items before it in the collection, in descending order. When we find a smaller item or reach the beginning of the collection, the loop breaks and we insert the item at the position that caused the loop to break.

```python
def insertion_sort(collection):
	for i in range(1, len(colleciton)):
		current_value = collection[i]
		position = i
		while position > 0 and collection[position-1] > current value:
			collection[position] = collection[position-1]
			postion -= 1
		collection[position] = current_value
```

---
### See also:
- [[What is an insertion sort?]]