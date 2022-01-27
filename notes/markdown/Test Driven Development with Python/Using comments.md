Note type: #litnote
Source: [[📖 Test Driven Development with Python]] ch2 p15

---
# Using comments
There should be caution when using comments. Having to use too many comments to explain the code usually means that the code has not been written clearly enough. In an ideal situation, the code should be so clear and so explicit that adding comments to explain it is unjustified.

Another thing to be wary of is that it's easy to forget to update comments when you change the functionality of the code that the comment describes, leading to misleading hints for future readers. Take the following example:
```python
wibble = 0

# Increments wibble by 1
wibble += 1
```

What happens if you later update it to this?
```python
wibble = 0

# Increments wibble by 1
wibble += 2
```

The comment no longer correctly explains what the code is doing, so always ask yourself if the code can be more clearly written when you feel the need to add explanatory comments.