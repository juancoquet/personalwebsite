Note type: #litnote
Source: [[📖 Effective Python]] Item 42

---
# Prefer protected attributes over private attributes
Since private attributes aren't enforced by the Python interpreter to allow overriding, it is best to make attributes protected (a single leading underscore) instead of private. This allows you and other users of your code to know when to proceed with caution when accessing a particular attribute without making it needlessly clunky. Always use documentation to explain attributes. Only consider using private attributes in order to avoid potential naming conflicts in the case that an attribute has a generic and common name that could easily be accidentally overwritten in sub-classes.

---
#### See also:
- [[Pythonic naming conventions]]