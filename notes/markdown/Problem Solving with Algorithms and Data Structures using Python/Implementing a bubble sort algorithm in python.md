Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.7
Date: 2021-11-04

---
# Implementing a bubble sort algorithm in python
To implement a bubble sort, we need to loop through the number of passes equal to the length of the list $n$ - 1, and within each pass iterate through the list up until the item at index `[-pass_num]`.

```python
def bubble_sort(collection):
	for pass_num in range(1, len(collection)):
		for i in range(len(collection) - pass_num):
			if collection[i] > collection[i+1]:
				collection[i], collection[i+1] = collection[i+1], collection[i]
```

The `range()` function is non-inclusive, meaning that for a `collection` of length 5 the first loop will iterate through the values 1, 2, 3, 4 giving us pass numbers up to $n-1$. We then use this pass number to create a range of indices that decrements with each pass in the next loop statement – if the `collection` length is 5, `range(len(collection) - pass_num)` iterates through the values 0, 1, 2, 3 on the first pass, 0, 1, 2 on the second pass, etc. We use these values to index into `collection` and compare the items found.

---
### See also:
- [[What is a bubble sort?]]