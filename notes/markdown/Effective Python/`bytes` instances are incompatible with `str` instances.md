Note type: #litnote
Source: [[📖 Effective Python]] item 3

---
# `bytes` instances are incompatible with `str` instances
`bytes` instances do not get on well with `str` instances and vise-versa. In order to use differing instances together, such as for concatenation or comparison, either the `bytes` instance must be decoded or the `str` instance must be encoded.

```python
bytes_instance.decode('utf-8')
# or
str_instance.encode('utf-8')
```