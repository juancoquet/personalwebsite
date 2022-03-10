Note type: #litnote
Source: [[📖 Effective Python]] item 69

---
# Using `decimal`
Python's `float` type is not always exact, which can lead to surprising results. When absolute precision is required, instead of using a `float` type you can pass the required number (before calculation) to the `Decimal` constructor.
```python
from decimcal import Decimal

print(Decimal('1.45'))		# passed as str
print(Decimal(1.45))		#passed as float

>>>
1.45
1.4499999999999999555910790149937383830547332763671875
```

The resulting number can then be used for calculations with absolute accuracy (be sure that all other numbers involved in the calculation are `Decimal` types in order to guarantee accuracy).