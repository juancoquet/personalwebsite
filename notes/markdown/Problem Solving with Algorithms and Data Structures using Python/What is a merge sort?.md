---
aliases: [merge sort]
Date: 2021-11-15
---
Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.11

---
# What is a merge sort?
Merge sort is a recursive divide and conquer algorithm for sorting a collection of items. It splits the collection into two halves recursively until it reaches a [[What is a base case?|base case]] with two split sub-lists of length 1 which are inherently sorted. Once this base case is reached, it begins to reassemble the sub-lists in order by comparing the left-most value of each list, and placing the smaller value at the beginning of the new composite list. Since the two sub-lists are already sorted, the lesser left-most value is always the smallest of all values within the two sub-lists being considered. This process continues until the all items have been reassembled into one (now ordered) list.

Considering a collection of length $n=8$, the algorithm first splits this into two lists of 4, then 4 lists of 2, and finally 8 lists of 1. These 8 lists of 1 are then combined into 4 ordered lists of length 2, then these 4 lists are combined into 2 ordered lists of length 4 and finally these 2 lists are combined into the full ordered list.

Recursive split:
$$[3, 5, 4, 6, 7, 1, 8, 2]$$
$$[3, 5, 4, 6]\:\:[7, 1, 8, 2]$$
$$[3, 5]\:\:[4, 6]\:\:[7, 1]\:\:[8, 2]$$
$$[3]\:\:[5]\:\:[4]\:\:[6]\:\:[7]\:\:[1]\:\:[8]\:\:[2]$$

Base case reached, merging commences:
$$[3, 5]\:\:[4, 6]\:\:[1, 7]\:\:[2, 8]$$
$$[3, 4, 5, 6]\:\:[1, 2, 7, 8]$$
$$[1, 2, 3, 4, 5, 6, 7, 8]$$

The splitting process runs $O(log\:n)$ times. For each of these $log\:n$ sub-lists, $n$ comparisons must me made, giving the merge sort algorithm a runtime function of $O(n\:log\:n)$.

---
### See also:
- [[The three characteristics of recursive algorithms]]