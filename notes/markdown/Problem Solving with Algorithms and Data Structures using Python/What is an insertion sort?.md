Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.9
Date: 2021-11-04

---
# What is an insertion sort?
An insertion sort maintains a sorted sub-list in the lower index positions of the list.

It starts with the assumption that a list of length 1 (the item at index 0) is inherently sorted, and sequentially 'inserts' one more item to this sub-list while maintaining its order with each new addition.

It maintains order by comparing the item currently being considered to each item in the ordered sub-list in descending order. Any items in the sorted sub-list that are greater than the item being considered are shifted to the right until the item at the start of the list is reached, or an item smaller than the item being considered is found. At this point, the new item is added to the list into the empty slot created by the prior positional shifts.