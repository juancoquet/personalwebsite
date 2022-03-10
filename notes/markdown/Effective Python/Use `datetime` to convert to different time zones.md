Note type: #litnote
Source: [[📖 Effective Python]] Item 67

---
# Use `datetime` to convert to different time zones
The `time` module is not the best for converting times to different time zones. It can convert to UTC time, but not to other time zones natively. To do this, use the `datetime` library instead.