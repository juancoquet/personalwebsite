---
aliases: [quick sort]
Date: 2021-11-29
---
Note Type: #litnote
Source: [[📖 Problem Solving with Algorithms and Data Structures using Python]] 6.12

---
# What is a quick sort?
A quick sort is a recursive divide and conquer algorithm for sorting a collection of items. With each recursion, one value is positioned into its corresponding place and all items to its left will be less than said value, while all values to its right will be greater than said value.

Assume we are sorting the following list:

`[54, 35, 12, 98, 14, 6, 77]`

The first step in a quick sort algorithm is selecting a *pivot value*. The pivot value is an element from the list to use for comparing and repositioning elements in subsequent steps. There are different ways of selecting the pivot value, but for this example we will simply select the first element from the list: 54.

`[{54}, 35, 12, 98, 14, 6, 77]`

With our pivot value selected, the next step is to compare each item in the collection to the pivot value using a *left marker* and a *right marker*. We will represent the left marker with `<>` and the right marker with `()`. To begin with, the markers are placed on the outer bounds of the list's items (ignoring the pivot value):

`[{54}, <35>, 12, 98, 14, 6, (77)]`

We then compare the value at the left marker to the pivot value. If the value is less than the pivot value, it can remain where it is and the position of the left marker moves to the right. In this example, 35 is less than 54 so the left marker moves to the next item:

`[{54}, 35, <12>, 98, 14, 6, (77)]`

Once again, 12 is less than 54 so the left value moves again:

`[{54}, 35, 12, <98>, 14, 6, (77)]`

This time, 98 is greater than 54. When this happens, we stop moving the left marker and shift our attention to the right marker. We execute a similar but opposing process with the right marker.

If the value at the right marker is greater than the pivot value, we leave it where it is and move the right marker to the left:

`[{54}, 35, 12, <98>, 14, (6), 77]`

This time, 6 is less than 54 so we stop moving the right marker. Now that we've found two out of place items (98 belongs to the right of the pivot value, 6 belongs to the left), we swap their positions:

`[{54}, 35, 12, <6>, 14, (98), 77]`

The markers then move inwards, and we begin the process again.

`[{54}, 35, 12, 6, <(14)>, 98, 77]`

14 is less than 54, so we move on:

`[{54}, 35, 12, 6, (14), <98>, 77]`

98 is greater than 54, so we stop. We now consider the value at the right marker. 14 is less than 54, so we stop. At this point, the index position of the right marker is less than the index position of the left marker. This means that the split point (the position where the pivot value belongs) has been found. When this occurs, we exchange the pivot value with the value at the right marker:

`[14, 35, 12, 6, ({54}), <98>, 77]`

Notice that now all values to the left of the pivot value are less than the pivot value, and all values to its right are greater than the pivot value. With the pivot value now in its correct position, the first recursion is done. We now call the quick sort algorithm again on the sub-list to the left and the sub-list to the right of the pivot value:

`[14, 35, 12, 6]`		`[98, 77]`

The base case is reached when the length of the list being quick sorted is less than or equal to 1 – such a list is inherently sorted.

The runtime function for a quick sort algorithm varies in the range between $O(log\:n)$ and $O(n^2)$ depending on where the pivot value belongs in the would-be sorted list. In a perfect world, the pivot value would belong in the middle of the list every time, meaning that with every iteration the list is split into two equal halves resulting in a $O(lon\:n)$ runtime function. However, the worst case scenario is that the pivot value is the smallest value in the list every time, meaning that with every recursion the quick sort function must be called on a left-list of length 0 and a right-list of length $n-1$, resulting in a $O(n^2)$ runtime function.

To more consistently get a pivot value that belongs near the middle of the sorted list, a technique called **median of three** can be used. This is where we consider the first element in the collection, the last element, and the element that is currently in the middle index position. We then choose the median of these three values as the pivot value. In our example, the first item is 54, the last 77 and the middle 98. The pivot value would be 77 in this case, which would actually give us worse performance than the original pivot value of 54, but it's clear to see how this method helps to reduce the variance of the runtime function and get it closer to the ideal $O(log\:n)$.