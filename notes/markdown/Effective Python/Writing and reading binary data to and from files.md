Note type: #litnote
Source: [[📖 Effective Python]] item 3

---
# Writing and reading binary data to and from files
Writing binary data to a file requires opening the file with writing binary `wb` mode:
```python
with open('file.bin', 'wb') as f:
	f.write(...)
```

Reading binary data from a file requires opening the file with read binary `rb` mode:
```python
with open('file.bin', 'rb') as f:
	data = f.read()
```

---
See also:
- [[`bytes` instances are incompatible with `str` instances]]