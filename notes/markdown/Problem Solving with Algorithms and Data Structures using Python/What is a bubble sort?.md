Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.7
Date: 2021-11-04

---
# What is a bubble sort?
A bubble sort algorithm makes multiple passes $p$ through a list of length $n$ where $p=n-1$, each time moving the largest unsorted item to its correct position at index $n-p$. It does this by first comparing the item at the start of the list (index $i=0$) to the next item in the list (index $i+1$). If the item at index $i$ is greater than the item at index $i+1$, their positions in the list are swapped around. If the item is not greater than the item next to it, they are not swapped and the larger of the two items will be used in the next comparison. After each comparison & swap cycle, the value of $i$ is incremented thus traversing the list.

The process continues, comparing the item at $i$ to the item at $i+1$ until the second to last item ($i=n-2$) is compared to the last item and swapped if necessary, meaning that the largest item now resides at the end of the list. At this point, the first pass is completed and one item (the largest in the collection) has been placed in its correct position.

Since the last item in the list is now in its proper place, we no longer need to compare items all the way to the list in the next pass. We only need to compare up to $i=n-3$, i.e. the third-from-last and second-from-last items. This process is repeated, making one less comparison with each pass until all passes have been made, at which point all members of the collection are in order.

The process for two passes is shown below:
<br>
$$5,2,3,1,4$$
$$(5,2),3,1,4 \rightarrow 2,5,3,1,4$$
$$2,(5,3),1,4 \rightarrow 2,3,5,1,4$$
$$2,3,(5,1),4 \rightarrow 2,3,1,5,4$$
$$2,3,1,(5,4) \rightarrow 2,3,1,4,5$$
<br>
$$(2,3),1,4,5 \rightarrow 2,3,1,4,5$$
$$2,(3,1),4,5 \rightarrow 2,1,3,4,5$$
$$2,1,(3,4),5 \rightarrow 2,1,3,4,5$$
