Note type: #litnote
Source: [[📖 Effective Python]] item 89

---
# The `warnings` module explained
The `warnings` module can be used to warn callers of your code that their present usage will soon be out of date, and they should update their code to meet new standards to prevent their code from breaking in the near future. The module is imported like any other warning, and warnings can be raised using the following syntax:
```python
import warnings

if arbitrary_condition:
	warnings.warn('this is my warning', DeprecationWarning)
```

This will raise a `DepracationWarning` at runtime—the code still runs, but a warning is printed to the console. This will encourage callers to update their code to prevent future breakages.