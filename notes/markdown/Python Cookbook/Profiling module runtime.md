Note type: #litnote
Source: [[📖 Python Cookbook]] ch14.13 p589

---
# Profiling module runtime
You can profile a module for a detailed breakdown of how each function runs by using `-m cProfile` from the command line:
```bash
bash % python3 -m cProfile somemodule.py
```

This will give you the following metrics for each function:
- `tottime`: total time spent *exclusively* in the function.
- `percall`: the average per call of the above.
- `cumtime`: the cumulative time spent in the function, and in any functions that the function calls.
- `percall`: the average per call of the above.