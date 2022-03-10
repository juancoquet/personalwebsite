Note type: #litnote
Source: [[📖 Effective Python]] item 37

---
# When nesting many built-in types becomes complicated, you should refactor into classes
Python makes it easy to nest built-in types like lists and dictionaries within each other, but that doesn't mean that this is the best approach. It can quickly become cumbersome and difficult to read, as well as difficult to work with. When you find that you are nesting more than one level of built-in types, it's time to refactor the code into classes.