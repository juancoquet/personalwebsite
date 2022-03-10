Note type: #litnote
Source: [[📖 Effective Python]] item 2

---
# Pythonic naming conventions
PEP 8 style guide suggests the following guidelines for naming different elements in your code:

- Functions, variables and attributes: `lowercase_underscore`
- Protected instances: `_leading_underscore`
- Private instance attributes: `__leading_dunder`
- Classes (including Exceptions): `CapitalisedWord`
- Module-level constants: `ALL_CAPS`
- Instance methods in classes use `self` to refer to the object as the first parameter
- Class methods use `cls` to refer to the class as the first parameter