Note type: #litnote
Source: [[📖 Python Cookbook]] ch3.16 p112

---
# Storing dates internally
It is common practice to store `date` and `datetime` objects internally in the UTC timezone to avoid any confusion and make working with dates much easier. These objects can then be translated and output in the user's local time when needed.