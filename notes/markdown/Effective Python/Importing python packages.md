Note type: #litnote
Source: [[📖 Effective Python]] item 85

---
# Importing python packages
Assume the following directory structure:
```
main.py
mypackage/__init__.py
mypackage/models.py
mypackage/nesteddir/anothermodule.py
mypackage/utils.py
```

The modules from `mypackage` can be imported into `main.py`:
```python
# main.py
from mypackage import utils
```

This dot-notation import statement is used for traversing through directories and modules. For example, I can go into a nested directory in the following manner:
```python
from mypackage.nesteddir import anothermodule
```

The same process can be followed to import an object from a particular module:
```python
from mypackage.nesteddir.anothermodule import thisfunction
```


---
#### See also:
- [[What are python packages]]