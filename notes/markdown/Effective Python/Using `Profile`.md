Note type: #litnote
Source: [[📖 Effective Python]] item 70

---
# Using `Profile`
The `cProfile` module offers functionality to measure the runtime performance of different objects. You simply make a `Profile` object, feed it the function you'l like to measure and then use `Stats` from the `pstats` module to print out statistics.
```python
from cProfile import Profile
from pstats import Stats

profiler = Profile
profiler.runcall(test)		# measureing a 'test' function

stats = Stats(profiler)		# making a stats object of the profile's data
stats.print_stats()		# print statistics
```

There are filtering and sorting methods available for `Stats` objects in order to make the return data more useful.

It's important to profile before beginning to optimise as the source of slow runtime is not always obvious, or it can be misleading. By profiling function calls you can see exactly which functions are responsible for slow runtime.