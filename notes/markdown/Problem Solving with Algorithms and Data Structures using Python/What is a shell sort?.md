Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]]
Date: 2021-11-14

---
# What is a shell sort?
A shell sort implements a variation on the insertion sort to improve runtime. It does this by separating the list into several sub-lists, then running an insertion sort on each sub-list. The initial number of sub-lists $s$ is calculated to be the length of the collection divided by 2, e.g. for a collection of $n=10$, we would begin with 5 sub-lists of length 2 (not every sub-list will necessarily have the same amount of items).

The items within each sub-list are not contiguous – each sub-list contains items that exist $s$ positions apart in the original collection. This means that the first sub-list consists of the items at index 0 and index 5, the second sub-list contains the items at index 1 and 6, etc. With the sub-lists identified, we then execute an insertion sort on their items.

Once an insertion sort has been run on each sub-list the value of $s$ is halved and the process is executed again. This means that for a collection of size $n=10$, the second iteration would have $s=2$ with each sub-list containing 5 items, each $s$ index positions apart.

The iterations finish when the value of $s$ reaches 0. Note that when $s=1$, this isn't really a sub-list – it's just a list containing all the items which, by this point, are much closer to their final ordered destinations. This means that the final insertion sort while $s=1$ does not need to make many changes.

The runtime function of a shell sort algorithms tends to fall somewhere between $O(n)$ and $O(n^2)$.

---
### See also:
- [[What is an insertion sort?]]