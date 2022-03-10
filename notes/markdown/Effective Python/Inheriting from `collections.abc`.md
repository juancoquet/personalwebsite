Note type: #litnote
Source: [[📖 Effective Python]] item 43

---
# Inheriting from `collections.abc`
Python's `collctions.abc` built in module is used for creating custom container types—that is, creating classes that inherit the functionality of Python's built in container types, like `list` or `dict`. This is so that you can create custom modified versions of these types to fit your needs.

Inheriting from these types requires that you import the module and then define the essential methods for that type, then Python will do the rest. An error will be raised if a required method goes undefined. This means that you do not have to define *every* method as you would if you inherited directly from `list`, for example. Instead you define the essential methods and the rest is automated.

This allows for uses like implementing a binary tree data structure that can be indexed like a list.