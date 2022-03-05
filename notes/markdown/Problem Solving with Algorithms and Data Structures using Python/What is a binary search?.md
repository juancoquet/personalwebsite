---
aliases: [Binary search,]
---
Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.4
Date: 2021-11-01

---
# What is a binary search?
Binary search is an algorithm that allows us to leverage the nature of an ordered list to dramatically decrease runtime.

When using a sequential search algorithm, we must consider each item in the collection being searched to see if it matches the item we are after. If the collection in question is ordered, we do not need to explicitly consider every item in the list before dismissing it as a non-match – this is what a binary search does.

A binary search recursively compares the item in the middle of an ordered list to the item being searched for. If the midpoint item matches, then `True` is returned. If the midpoint item is greater than the item being searched for, then we know implicitly that all subsequent items must also be greater than the search query as the list is ordered, and thus they are *not* the search query. The inverse applies if the midpoint item is less than the item being searched for – all items prior to the midpoint item must also be less than the item being searched for, and therefore not a match.

This implicit knowledge allows us to instantly dismiss half of the items in the list if a match is not found. We then execute the function again, following the same steps, but this time only on the half of the list that remains. Eventually, either the midpoint item will return a match, or the collection will be whittled down to zero members – at which point `False` can be returned as the search item was not found in the collection.

Binary search implements a **divide and conquer** strategy – it divides a large problem into smaller pieces and then reassembles the pieces to return a solution.

---
### See also:
- [[What is sequential search?]]