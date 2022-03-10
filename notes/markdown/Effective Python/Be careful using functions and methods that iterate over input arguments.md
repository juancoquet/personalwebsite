Note type: #litnote
Source: [[📖 Effective Python]] Item 31

---
# Be careful using functions and methods that iterate over input arguments
Since iterators are exhaustible, this can cause strange behaviour when using functions and methods that iterate over input arguments. If an iterator is passed in instead of an iterable container, it's possible that the iterator will be exhausted before the function has finished using it—for example, if a function needs to iterate through an input argument twice or more, in the case that an iterator is passed in it will be exhausted after the first iteration and the following calls to iterate over the input will not function as expected.

---
#### See also:
- [[Iterables are not the same as iterators]]