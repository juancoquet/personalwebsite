Note type: #litnote
Source: [[📖 Python Cookbook]] ch14.13 p589

---
# Timing a function call with `timetit()`
The `timeit` module can be imported to time a function call. It takes three arguments—the first is a string containing the function you wish to time (with arguments included), the second is another string that runs before the function call to prepare the environment (import statements go here) and the third argument is the number of times the function should be run, which default to one million.
```python
from timeit import timeit

timeit('math.sqrt(4)', 'import math', number=1000000)
```