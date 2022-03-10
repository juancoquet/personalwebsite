Note type: #litnote
Source: [[📖 Effective Python]] Item 31

---
# Iterables are not the same as iterators
An *iterable* is any object that can be *iterated over*. That is, an iterable is any object that can be *turned into* an iterator—either implicitly (when called in a `for` loop) or explicitly by using `iter()`. They can be iterated over but they are not iterators in and of themselves.

An *iterator*, on the other hand, needs no further modification in order to be iterated over. Iterators implement the built-in `__iter__` and `next` methods to allow iteration, whereas iterables cannot do this without first being turned into an iterator.

The main difference is that *iterables can be reused* and *iterators cannot be reused*. Once an iterator has been iterated over, it is exhausted and further calls to the `next` method will not return any values. By contrast, iterables are simply *containers* of data that can be turned into a new iterator an indefinite number of times.